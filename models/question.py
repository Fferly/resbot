import peewee as pw

from base_model import BaseModel
from test import Test

class Question(BaseModel):
    id = pw.AutoField()
    test_id = pw.ForeignKeyField(Test, backref='questions')
    title = pw.CharField()
