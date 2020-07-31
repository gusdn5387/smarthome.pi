from dataclasses import dataclass
import RPi.GPIO as GPIO

from .add_to_dashboard import add_ledstatus_to_dashboard


@dataclass
class Led:
    output: int
    is_on: bool = False

    def __post_init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.output, GPIO.OUT)

    def on(self):
        if self.is_on == True:
            pass
        else:
            self.is_on = True
            GPIO.output(self.output, True)
            add_ledstatus_to_dashboard(True)
    
    def off(self):
        if self.is_on == False:
            pass
        else:
            self.is_on = False
            GPIO.output(self.output, False)
            add_ledstatus_to_dashboard(False)
