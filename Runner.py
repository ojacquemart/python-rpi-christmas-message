#!/usr/bin/python

from time import sleep

from Adafruit_CharLCD import Adafruit_CharLCD
from Messages import *


class Runner:
    scenario = None
    lcd = Adafruit_CharLCD()

    def __init__(self, scenario):
        self.scenario = scenario

    def run(self):
        while 1:
            for item in self.scenario.items:
                content = item.getContent()

                self.lcd.clear()
                self.lcd.message(content.message)

                sleep(content.duration)


if __name__ == '__main__':
    scenario = SimpleScenario.get()

    runner = Runner(scenario)
    runner.run()
