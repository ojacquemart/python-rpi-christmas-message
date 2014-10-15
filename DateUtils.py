#!/usr/bin/python

import datetime
import os

class DateUtils:

    WEEK_DAYS = [ 'Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi' ]

    @staticmethod
    def daysUntilChristmas():
        today = datetime.date.today()
        christmasDay = datetime.date(today.year, 12, 25)
        diff = christmasDay - today

        return diff.days

    @staticmethod
    def isChristmasDay():
        today = datetime.date.today()

        return today.day == 25 and today.month == 12

    @staticmethod
    def getDayOfWeek():
        dayOfWeek = int(datetime.datetime.today().strftime('%w'))

        return DateUtils.WEEK_DAYS[dayOfWeek]