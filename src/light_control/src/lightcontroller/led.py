from dataclasses import dataclass
from flask import Flask

app = Flask(__name__)
if app.env == 'development':
    import FakeRPi.GPIO as GPIO
else:
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