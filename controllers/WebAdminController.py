from flask import Flask, request

from controllers.StudentController import StudentController
from controllers.TestController    import TestController


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

            TestController.add_test(test_title, test_max_points)

            questions = request.form['questions_json']
            print(questions)

            return WebAdminView.redirect_to_add_test()
        return WebAdminView.show_add_test()

    def add_student(self):
        if request.method == 'POST':
            student_name = request.form['student_name']
            student_group = request.form['student_group']
            StudentController.create_student(
                student_name, student_group
            )
            return WebAdminView.redirect_to_add_student()
        return WebAdminView.show_add_student()

    def tests(self):
        pass

    def students(self):
        students = StudentController.get_all_students()
        return WebAdminView.show_students(students)
