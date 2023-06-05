from views.TelegramBotView import TelegramBotView

class TelegramBotController:
    def __init__(self, db):
        self.view = TelegramBotView()
        self.db = db   
