from dataclasses import dataclass, field
import RPi.GPIO as GPIO


@dataclass
class Motor:
    output: int
    gpio_pwm = field(init=False)
    mode_cool: bool = True

    def __post_init__(self):
        GPIO.setmode(GPIO.BCM)
        self.gpio_pwm = GPIO.PWM(self.output, 50)
        self.gpio_pwm.start(0)
        
        self.set_hot()

    def move(self, angle: float):
        duty = angle / 10.0 + 2.5
        self.gpio_pwm.ChangeDutyCycle(duty)

    def set_cool(self):
        if self.mode_cool == True:
            return False
        
        self.move(0)
        self.mode_cool = True
        return True

    def set_hot(self):
        if self.mode_cool == False:
            return False

        self.move(30)
        self.mode_cool = False
        return True


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

    def off(self):
        if self.is_on == False:
            pass
        else:
            self.is_on = False
            GPIO.output(self.output, False)

@dataclass
class Airconditioner:
    led: Led
    motor: Motor
    mode_cool: bool = False
    
    def set_hot(self):
        if self.mode_cool == False:
            return False
        self.motor.set_hot()
        self.led.off()
        self.mode_cool = False

    def set_cool(self):
        if self.mode_cool == True:
            return False
        self.motor.set_cool()
        self.led.on()
        self.mode_cool = True
