import telebot

from controllers.TestController import TestController
from views.TelegramBotView import TelegramBotView

from resources.config import bot_token

bot = telebot.TeleBot(bot_token);


class TelegramBotController:
    @staticmethod
    def get_bot():
        return bot

    @staticmethod
    @bot.message_handler(func=lambda message: message.text == '/start')
    def handle_start(message):
        TelegramBotView.show_start(bot, message)

    @staticmethod
    @bot.message_handler(func=lambda message: message.text == '/tests')
    def handle_tests(message):
        tests = TestController.get_all_tests()
        test_names = []


        for test in tests:
            test_names.append(
                test.title
            )

        TelegramBotView.show_tests(bot, message, test_names)


    @staticmethod
    def handle_results():
        pass

    
