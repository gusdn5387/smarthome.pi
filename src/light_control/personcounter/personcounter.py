from .ultrasonicsensor import Ultrasonicsensor, UltrasonicsensorPair, CloseDetected, CloseDetectedPair
from add_to_dashboard import add_roomstatus_to_dashboard


class PersonCounter:
    """
    Ultrasonicsensor 2개를 통해 사람의 움직임을 감지하여 방 안 사람의 수를 체크함
    """

    def __init__(self, inner: Ultrasonicsensor, outer: Ultrasonicsensor) -> None:
        self.ultrasonicsensor_pair: UltrasonicsensorPair = UltrasonicsensorPair(
            inner=inner, outer=outer)
        self.closedetected_pair: CloseDetectedPair = CloseDetectedPair(
            CloseDetected(), CloseDetected())
        self.person_count = 0

    def get_room_person_count(self) -> int:
        if self.ultrasonicsensor_pair.inner.is_close_detected():
            self.closedetected_pair.inner.set_close_detected(close_detected=True)

        if self.ultrasonicsensor_pair.outer.is_close_detected():
            self.closedetected_pair.outer.set_close_detected(close_detected=True)

        if self.closedetected_pair.did_person_left_room() == True:
            self.person_count = self.person_count - 1
            add_roomstatus_to_dashboard(self.person_count)
            if self.person_count < 0:
                raise ValueError(f"person_count {self.person_count} < 0")
        elif self.closedetected_pair.did_person_enter_room() == False:
            self.person_count = self.person_count + 1
            add_roomstatus_to_dashboard(self.person_count)
        
        return self.person_count
