class TelegramBotView:
    @staticmethod
    def show_start(bot, message):
        answer = 'Вітаю вас у Resbot! Що здаємо сьогодні?'
        bot.send_message(message.chat.id, answer)
        