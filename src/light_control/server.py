from flask import Flask

from personcounter.ultrasonicsensor import Ultrasonicsensor
from personcounter.personcounter import PersonCounter
from lightcontroller.led import Led

app = Flask(__name__)

personcounter = PersonCounter(
    inner = Ultrasonicsensor(gpio_trigger=18, gpio_echo=24, close_throttle_cm=8),
    outer = Ultrasonicsensor(gpio_trigger=25, gpio_echo=23, close_throttle_cm=8)
)

led = Led(output=26)

@app.route("/")
def home():
    return "People counting & Automated Light Control system"

@app.route("/room/people/count")
def get_room_person_count():
    """
    현재 방에 있는 사람 수를 리턴함
    """
    return str(personcounter.get_room_person_count())


@app.route("/room/light/update")
def update_light_onoff():
    """
    방 안에 있는 사람의 수를 구한 뒤 방의 전등 상태를 업데이트함
    """
    perosn_count = personcounter.get_room_person_count()
    print(perosn_count)
    if perosn_count > 0:
        print("led off")
        led.off()
    else:
        print("led on")
        led.on()
    
    return 'ok'


if __name__ == "__main__":
    app.run()
