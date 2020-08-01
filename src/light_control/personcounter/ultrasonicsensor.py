from dataclasses import dataclass
import time
import datetime

import RPi.GPIO as GPIO


@dataclass
class Ultrasonicsensor:
    gpio_trigger: int
    gpio_echo: int
    close_throttle_cm: float

    def __post_init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_trigger, GPIO.OUT)
        GPIO.setup(self.gpio_echo, GPIO.IN)

    def _get_distance(self) -> float:
        GPIO.output(self.gpio_trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.gpio_trigger, False)
        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.gpio_echo) == 0:
            start_time = time.time()

        while GPIO.input(self.gpio_echo) == 1:
            stop_time = time.time()

        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2

        return distance

    def is_close_detected(self) -> bool:
        distance = self._get_distance()
        if distance < self.close_throttle_cm:
            return True
        else:
            return False


@dataclass
class UltrasonicsensorPair:
    inner: Ultrasonicsensor
    outer: Ultrasonicsensor


@dataclass
class CloseDetected:
    close_detected = False
    detected_at: datetime.datetime = datetime.datetime.now()

    def reset(self):
        self.close_detected = False
        self.detected_at = datetime.datetime.now()
        

    def set_close_detected(self, close_detected: bool) -> bool:
        """
        close_detected 값을 업데이트함. 
        """
        since_close_detected_updated_to_true = datetime.datetime.now() - self.detected_at
        if since_close_detected_updated_to_true.total_seconds() < 3 or self.close_detected == close_detected:
            return False
        else:
            self.detected_at = datetime.datetime.now()
            self.close_detected = close_detected
            print(f"detaction updated: {self.close_detected}")
            return True


@dataclass
class CloseDetectedPair:
    inner: CloseDetected
    outer: CloseDetected

    def reset(self):
        self.inner.reset()
        self.outer.reset()

    def did_person_left_room(self, inner_close_detected) -> bool:
        if inner_close_detected is True and self.inner.close_detected is True:
            self.reset()
            return True
        else:
            return False

    def did_person_enter_room(self, outer_close_detected) -> bool:
        if outer_close_detected is True and self.outer.close_detected is True:
            self.reset()
            return True
        else:
            return False
