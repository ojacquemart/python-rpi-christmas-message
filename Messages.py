#!/usr/bin/python

import time
from DateUtils import DateUtils


class SimpleScenario:
    @staticmethod
    def get():
        items = [
            DayDateMessage(),
            TimeMessage(),
            ChristmasMessage()
        ]

        return Scenario(items)


class Scenario:
    items = []

    def __init__(self, items):
        self.items = items


class TimeMessage:
    def getContent(self):
        row1 = MessageRow("Il est")
        row2 = MessageRow(time.strftime("%T"))

        return Message(5, row1 + row2)


class DayDateMessage:
    def getContent(self):
        row1 = MessageRow(DateUtils.getDayOfWeek())
        row2 = MessageRow(time.strftime("%d/%m/%Y"))

        return Message(5, row1 + row2)


class ChristmasMessage:
    DURATION = 10

    def getContent(self):
        if DateUtils.isChristmasDay():
            return Message(self.DURATION, MessageRow("C'est Noel!"))
        else:
            row1 = MessageRow(str(DateUtils.daysUntilChristmas()) + " jours")
            row2 = MessageRow("avant Noel")

            return Message(self.DURATION, row1 + row2)


class Message:
    duration = 0
    message = ""

    def __init__(self, duration, message):
        self.duration = duration
        self.message = message


class MessageRow:
    MAX_LENGTH = 16
    message = ""

    def __init__(self, message):
        self.message = message

    def __getRow(self):
        return self.spaces() + self.message

    def spaces(self):
        return " " * self.spacesBeforeMessage()

    def spacesBeforeMessage(self):
        return self.length() / 2

    def length(self):
        return self.MAX_LENGTH - len(self.message)

    def __str__(self):
        return self.__getRow()

    def __add__(self, other):
        return self.__getRow() + "\n" + other.__getRow()
