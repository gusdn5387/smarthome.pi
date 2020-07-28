from dataclasses import dataclass
from flask import Flask

import RPi.GPIO as GPIO


@dataclass
class Led:
    output: int

    def __post_init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.output, GPIO.OUT)

    def on(self):
        GPIO.output(self.output, True)
    
    def off(self):
        GPIO.output(self.output, False)