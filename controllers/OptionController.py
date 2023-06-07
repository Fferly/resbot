from models.option import Option

class OptionController:
    @staticmethod
    def add_option(question_id, text, is_right):
        option = Option.create(
            question_id=question_id, 
            text=text, 
            is_right=is_right
        )
        return option

    @staticmethod
    def get_options_by_question_id(question_id):
        options = list(
            Option.select()
                .where(Option.question_id == question_id)
                .execute()
        )
        return options
