import datetime
from dataclasses import dataclass, field
import board
import adafruit_dht

@dataclass
class Dht11:
    temperature: float = field(init=False)
    dht_device: adafruit_dht.DHT11 = field(init=False)
    updated_at: datetime.datetime = datetime.datetime.now()

    def __post_init__(self):
        self.dht_device = adafruit_dht.DHT11(board.D17)
    
    def get_temperature(self) -> float:
        if (datetime.datetime.now() - self.updated_at).total_seconds() > 3:
            self.updated_at = datetime.datetime.now()
            self.temperature = self.dht_device.temperature

        return self.temperature
    
    def get_humidity(self) -> float:
        return self.dht_device.humidity

