from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

class TelegramBotView:
    @staticmethod
    def show_start(bot, message):
        answer = 'Вітаю вас у Resbot! Що здаємо сьогодні?'
        bot.send_message(message.chat.id, answer)

    @staticmethod
    def show_tests(bot, message, test_names):
        keyboard = InlineKeyboardMarkup()

        for name in test_names:
            button = InlineKeyboardButton(name, callback_data=name)
            keyboard.add(button)

        answer = 'Вам доступні наступні тести, оберіть потрібний'

        bot.send_message(message.chat.id, answer, reply_markup=keyboard)
    
        