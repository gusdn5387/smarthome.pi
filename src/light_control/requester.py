from . import server
import time

while True:
    server.update_light_onoff()
    time.sleep(0.1)