from flask import Flask

from resources.config import project_name 
from views.WebAdminView import WebAdminView


class WebAdminController:
    def __init__(self, db):
        self.view = WebAdminView()
        self.db = db
        self.app = Flask(project_name)

    def run_app(self):
        self.app.run()

    def create_test():
        pass

    def add_student(self):
        return self.view.show_add_student()

    def view_tests():
        pass

    def view_students(self):
        students = []
        return self.view.show_students(students)

