from controllers.WebAdminController    import WebAdminController
from controllers.TelegramBotController import TelegramBotController

from models.option   import Option
from models.question import Question 
from models.result   import Result
from models.student  import Student
from models.test     import Test

from utils.database import Database


class AppController:
    def __init__(self):
        self.db = Database().get_connection()

    def run_app(self):
        self.db.create_tables(
           [Student, Test, Question, Option, Result]
        )

        web_controller = WebAdminController(self.db)
        bot_controller = TelegramBotController(self.db)

        app = web_controller.app
        app.add_url_rule('/admin/create_test', view_func=web_controller.create_test)
        app.add_url_rule('/admin/add_student', view_func=web_controller.add_student)
        app.add_url_rule('/admin/tests',       view_func=web_controller.view_tests)
        app.add_url_rule('/admin/students',    view_func=web_controller.view_students)


        web_controller.run_app()
        bot_controller.run_app()   


