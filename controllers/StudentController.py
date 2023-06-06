from models.student import Student

class StudentController:
    @staticmethod
    def create_student(name, group):
        student = Student.create(
            name=name,
            group=group
        )
        return student
    
    @staticmethod
    def get_all_students():
        return list(Student.select().execute())
    