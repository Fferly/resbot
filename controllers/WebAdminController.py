from flask import Flask, request

from controllers.StudentController import StudentController
from views.WebAdminView import WebAdminView

from resources.config import project_name 


class WebAdminController:
    def __init__(self):
        self.app = Flask(project_name)

    def run_app(self):
        self.app.run()

    def create_test():
        pass

    def add_student(self):
        if request.method == 'POST':
            student_name = request.form['student_name']
            student_group = request.form['student_group']
            StudentController.create_student(
                student_name, student_group
            )
            return WebAdminView.redirect_to_add_student()
        return WebAdminView.show_add_student()

    def tests():
        pass

    def students(self):
        students = StudentController.get_all_students()
        return WebAdminView.show_students(students)
