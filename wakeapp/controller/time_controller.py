from datetime import datetime, time
from typing import Tuple

from wakeapp.utils.regex_utils import check_string


class TimeController:
    def __init__(self, arrival:datetime=None, depature:datetime=None) -> None:
        if arrival is None:
            self.arrival = datetime.now()
        if depature is None:
            self.depature = datetime.now()

    def calculate_travel_time(self) -> Tuple[str,str,str]:
        """Return a Tuple of hour, minute and second calculated by the internal arrival and depature time"""
        time_diff = self.arrival - self.depature
        return (str(time_diff).split(":"))

    
    def get_wakeup_datetime(self, get_ready: time) -> datetime:
        hours, minutes, seconds = self.calculate_travel_time()
        travel_time = time(hour=hours, minute=minutes, seconds=seconds)
        

    def convert_string_to_time_object(time: str) -> time | None:
        if (check_string(time, r"^[012]\d:[0-5]\d$")):
            return None
        (hour, minutes) = time.split(":")
        return time(hour=hour, minute=minutes)
