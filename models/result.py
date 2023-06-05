import peewee as pw 

from base_model import BaseModel
from student import Student
from test import Test 

class Result(BaseModel):
    id = pw.AutoField()
    stud_id = pw.ForeignKeyField(Student, backref='results')
    test_id = pw.ForeignKeyField(Test, backref='results')
    