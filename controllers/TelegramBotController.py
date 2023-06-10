import telebot

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
    def handle_tests(self):
        pass

    @staticmethod
    def handle_results():
        pass

    
