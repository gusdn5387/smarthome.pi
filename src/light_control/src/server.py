from flask import Flask
import time

from personcounter.ultrasonicsensor import Ultrasonicsensor
from personcounter.personcounter import PersonCounter

app = Flask(__name__)

personcounter = PersonCounter(
    inner = Ultrasonicsensor(gpio_trigger=18, gpio_echo=24, close_throttle_value=8),
    outer = Ultrasonicsensor(gpio_trigger=25, gpio_echo=23, close_throttle_value=8)
)

@app.route("/")
def home():
    return "people counting system"

@app.route("/room/people/count")
def get_room_person_count():
    return str(personcounter.get_room_person_count())

if __name__ == "__main__":
    app.run()

