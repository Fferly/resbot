import peewee as pw 
from base_model import BaseModel

class Student(BaseModel):
    id = pw.AutoField()
    name = pw.CharField()
    group = pw.CharField
