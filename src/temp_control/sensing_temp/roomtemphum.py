from dataclasses import dataclass, field
from enum import Enum, auto
import datetime

from .dht11 import Dht11


class AutoAirConditionMode(Enum):
    COOL = auto()
    HOT = auto()


@dataclass
class AutoAirConditioning:
    threshold_temp: float
    threshold_hum: float
    dth11: Dht11
    autoaircondition_mode = AutoAirConditionMode.HOT


    def update_autoaircondition_mode(self):
        temp = self.dth11.get_temperature()
        # hum = self.dth11.get_humidity()

        if temp >= self.threshold_temp:
            self.autoaircondition_mode = AutoAirConditionMode.COOL
        else:
            self.autoaircondition_mode = AutoAirConditionMode.HOT
