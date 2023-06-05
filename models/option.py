import peewee as pw

from base_model import BaseModel
from question import Question

class Option(BaseModel):
    id = pw.AutoField()
    question_id = pw.ForeignKeyField(Question, backref='questions')
    text = pw.CharField()
    is_right = pw.BooleanField()
