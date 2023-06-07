from models.test import Test

class TestController:
    @staticmethod
    def add_test(title, max_points):
        test = Test.create(
            title=title,
            max_points=max_points
        )
        return test

    @staticmethod
    def get_all_tests():
        return list(Test.select().execute())
    