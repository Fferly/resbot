from controllers.WebAdminController import WebAdminController
from utils.database import Database

from models.base_model import BaseModel
from models.option import Option
from models.question import Question 
from models.result import Result
from models.student import Student
from models.test import Test


if __name__ == '__main__':
    db = Database().get_connection().create_tables(
        [Student, Test, Question, Option, Result]
    )

    web_controller = WebAdminController()

