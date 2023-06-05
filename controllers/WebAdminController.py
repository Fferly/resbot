from flask import Flask, render_template, request

from resources.config import project_name 
from views.WebAdminView import WebAdminView

app = Flask(project_name)

class WebAdminController:
    def __init__(self):
        self.view = WebAdminView()

    @app.route('/admin/create_test', methods=['GET','POST'])
    def create_test():
        pass

    @app.route('/admin/view_tests', methods=['GET'])
    def view_tests():
        pass

    @app.route('/admin/add_student', methods=['GET','POST'])
    def add_student():
        pass
