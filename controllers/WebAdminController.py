import json
from flask import Flask, request

from controllers.StudentController  import StudentController
from controllers.TestController     import TestController
from controllers.QuestionController import QuestionController
from controllers.OptionController   import OptionController

from views.WebAdminView import WebAdminView

from resources.config import project_name 


class WebAdminController:
    def __init__(self):
        self.app = Flask(project_name)

    def run_app(self):
        self.app.run()

    def add_test(self):
        if request.method == 'POST':
            test_title = request.form['test_title']
            test_max_points = request.form['max_points']

            addedTest = TestController.add_test(test_title, test_max_points)

            questions = json.loads(request.form['questions_json']).values()
            
            for question in questions:
                addedQuestion = QuestionController.add_question(
                    title=question['title'],
                    test_id=addedTest.id
                )

                options = question['options']

                for option in options:
                    OptionController.add_option(
                        text=option['text'],
                        is_right=option['isRight'],
                        question_id=addedQuestion.id
                    )

            return WebAdminView.redirect_to_add_test()
        return WebAdminView.show_add_test()

    def add_student(self):
        if request.method == 'POST':
            student_name = request.form['student_name']
            student_group = request.form['student_group']
            student_tg = request.form['student_tg']
            StudentController.create_student(
                student_name, student_group, student_tg
            )
            return WebAdminView.redirect_to_add_student()
        return WebAdminView.show_add_student()

    def tests(self):
        tests = TestController.get_all_tests()
        testsToRender = []

        for test in tests:
            testToAdd = {}
            testToAdd['title'] = test.title
            testToAdd['questions'] = []

            questions = QuestionController.get_questions_by_test_id(
                test_id=test.id
            )

            for question in questions:
                questionToAdd = {}
                questionToAdd['title'] = question.title
                questionToAdd['options'] = OptionController.get_options_by_question_id(
                    question_id=question.id
                )
            
                testToAdd['questions'].append(questionToAdd)
        
            testsToRender.append(testToAdd)

        print(testsToRender)
        return WebAdminView.show_tests(testsToRender)

    def students(self):
        students = StudentController.get_all_students()
        return WebAdminView.show_students(students)
