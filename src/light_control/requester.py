from server import update_light_onoff
import time

while True:
    update_light_onoff()
    time.sleep(0.1)