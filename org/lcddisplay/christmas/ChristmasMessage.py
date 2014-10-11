import datetime

from Adafruit_CharLCD import Adafruit_CharLCD

class ChristmasMessage:

    def display(self):
        lcd = Adafruit_CharLCD()
        lcd.clear()

        lcd.message(NbDaysRow.get())
        lcd.message(BeforeChristmasRow.get())


class NbDaysRow:

    @staticmethod
    def get():
        days = DateUtils.daysUntilChristmas()

        return MessageRow(str(days) + " days").get()


class BeforeChristmasRow:

    @staticmethod
    def get():
        return MessageRow("before Christmas").get()

class MessageRow:

    MAX_LENGTH = 16
    message = ""

    def __init__(self, message):
        self.message = message

    def get(self):
        return self.spaces() + self.message

    def spaces(self):
        spaces = ""

        spacesBeforeMessage = self.spacesBeforeMessage()
        for i in range(0, spacesBeforeMessage):
            spaces += " "

        return spaces

    def spacesBeforeMessage(self):
        return self.length() / 2

    def length(self):
        return self.MAX_LENGTH - len(self.message)


class DateUtils:

    @staticmethod
    def daysUntilChristmas():
        today = datetime.date.today()
        christmasDay = datetime.date(2014, 12, 25)
        diff = christmasDay - today

        return diff.days


def hello():
    print NbDaysRow.get()
    print BeforeChristmasRow.get()

if __name__ == '__main__':
    hello()
