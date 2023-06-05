from peewee import SqliteDatabase

from resources.config import db_name

from models.base_model import BaseModel
from models.option import Option
from models.question import Question 
from models.result import Result
from models.student import Student
from models.test import Test


class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            db = SqliteDatabase('resbot.db')
            BaseModel._meta.database = db
            cls._instance.db = db


            cls._instance.db.create_tables(
                [Student, Test, Question, Option, Result]
            )
        return cls._instance

    def get_connection(self):
        return self.db
