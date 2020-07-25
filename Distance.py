import RPi.GPIO as GPIO
import time
from typing import Tuple

GPIO.setmode(GPIO.BCM)
 
#You can use whichever GPIO pins you want
LEFT_GPIO_TRIGGER = 18
LEFT_GPIO_ECHO = 24

RIGHT_GPIO_TRIGGER = 25
RIGHT_GPIO_ECHO = 23

GPIO.setup(LEFT_GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(LEFT_GPIO_ECHO, GPIO.IN)

GPIO.setup(RIGHT_GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(RIGHT_GPIO_ECHO, GPIO.IN)

def get_distance(trigger_pin: int, echo_pin: int, name: str = "sensor") -> float:
    print(f"{name} start, setup")
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)
    start_time = time.time()
    stop_time = time.time()

    print(f"{name} while 1")
    while GPIO.input(echo_pin) == 0:
        start_time = time.time()

    print(f"{name} while 2")
    while GPIO.input(echo_pin) == 1:
        stop_time = time.time()
    
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance

# def distance() -> Tuple[float, float]:
#     print("LEFT SETUP")
#     GPIO.output(LEFT_GPIO_TRIGGER, True)
#     time.sleep(0.00001)
#     GPIO.output(LEFT_GPIO_TRIGGER, False)
    
#     print("RIGHT SETUP")
#     GPIO.output(RIGHT_GPIO_TRIGGER, True)
#     time.sleep(0.00001)
#     GPIO.output(RIGHT_GPIO_TRIGGER, False)
 
#     left_start_time = time.time()
#     left_stop_time = time.time()

#     right_start_time = time.time()
#     right_stop_time = time.time()

#     print("LEFT GPIO WHILE 1")
#     while GPIO.input(LEFT_GPIO_ECHO) == 0:
#         left_start_time = time.time()
#     print("LEFT GPIO WHILE 2")
#     while GPIO.input(LEFT_GPIO_ECHO) == 1:
#         left_stop_time = time.time()

#     print("RIGHT GPIO WHILE 1")
#     while GPIO.input(RIGHT_GPIO_ECHO) == 0:
#         right_start_time = time.time() 
#     print("RIGHT GPIO WHILE 2")
#     while GPIO.input(RIGHT_GPIO_ECHO) == 1:
#         right_stop_time = time.time()
 
#     left_time_elapsed = left_stop_time - left_start_time
#     left_distance = (left_time_elapsed * 34300) / 2

#     right_time_elapsed = right_stop_time - right_start_time
#     right_distance = (right_time_elapsed * 34300) / 2
 
#     return (left_distance, right_distance)
 
if __name__ == '__main__':
    try:
        while True:
            left_distance = get_distance(LEFT_GPIO_TRIGGER, LEFT_GPIO_ECHO)
            right_distance = get_distance(RIGHT_GPIO_TRIGGER, RIGHT_GPIO_ECHO)
            # dist = distance()
            print(f"left = {left_distance:.2f}, right = {right_distance:.2f}")
            time.sleep(1)
 
    except KeyboardInterrupt:
        print("Program stopped by User")
        GPIO.cleanup()