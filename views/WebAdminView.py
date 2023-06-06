from flask import redirect, render_template

class WebAdminView:
    def show_students(self, students):
        return render_template('students.html', students=students)

    @staticmethod
    def show_tests(tests):
        pass

    @staticmethod
    def show_add_test():
        pass

    @staticmethod
    def show_add_student():
        return render_template('add_student.jinja')

    @staticmethod
    def redirect_to_students():
        pass

    @staticmethod
    def redirect_to_tests():
        pass

    @staticmethod
    def redirect_to_add_students():
        pass

    @staticmethod
    def reirect_to_add_test():
        pass
