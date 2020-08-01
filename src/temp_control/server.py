from flask import Flask

from sensing_temp.roomtemphum import AutoAirConditioning, AutoAirConditionMode, Dht11
from tempcontrol.airconditioner import Airconditioner, Led, Motor

app = Flask(__name__)

airconditioner = Airconditioner(led=Led(output=13), motor=Motor(output=19))
autoairconditioning = AutoAirConditioning(
    threshold_temp=27, threshold_hum=50, dth11=Dht11()
)


@app.route("/")
def home():
    return "Temperature Sensing & Automated Temperature Control system"


@app.route("/room/temp")
def get_room_temp():
    """
    현재 방의 온도를 리턴함
    """
    return str(autoairconditioning.dth11.get_temperature())


@app.route("/room/airconditioner/update")
def update_airconditioner_coolhot():
    """
    방 안에 있는 사람의 수를 구한 뒤 방의 전등 상태를 업데이트함
    """
    autoairconditioning.update_autoaircondition_mode()

    if autoairconditioning.autoaircondition_mode == AutoAirConditionMode.COOL:
        print("cooling on")
        airconditioner.set_cool()
    else:
        print("cooling off")
        airconditioner.set_hot()

    return "ok"


if __name__ == "__main__":
    app.run()
