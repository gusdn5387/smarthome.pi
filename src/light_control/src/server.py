from flask import Flask
import time
from dataclasses import dataclass

app = Flask(__name__)

if app.env == 'development':
    import FakeRPi.GPIO as GPIO
else:
    import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

@dataclass
class UltrasonicSensor:
    gpio_trigger: int
    gpio_echo: int

    def setup_gpio(self):
        GPIO.setup(self.gpio_trigger, GPIO.OUT)
        GPIO.setup(self.gpio_echo, GPIO.IN)

inner = UltrasonicSensor(gpio_trigger=18, gpio_echo=24)
outer = UltrasonicSensor(gpio_trigger=25, gpio_echo=23)

def get_distance(trigger_pin: int, echo_pin: int, name: str = "sensor") -> float:
    # print(f"{name} start, setup")
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)
    start_time = time.time()
    stop_time = time.time()

    # print(f"{name} while 1")
    while GPIO.input(echo_pin) == 0:
        start_time = time.time()

    # print(f"{name} while 2")
    while GPIO.input(echo_pin) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sensors/inner/")
def wow():
    inner.setup_gpio()
    return str(get_distance(inner.gpio_trigger, inner.gpio_echo))

# @app.route("/sensors/outer/")
# def get_outer_distance():
#     return get_distance(outer.gpio_trigger, outer.gpio_echo)

# @app.route("/sensors/")
# def get_sensors_distances():
#     return {
#         inner: get_inner_distance(),
#         outer: get_outer_distance()
#     }


if __name__ == "__main__":
    # outer.setup_gpio()
    app.run()

