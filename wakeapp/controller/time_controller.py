from datetime import datetime, time, timedelta


class TimeController:
    def __init__(self, arrival:datetime=None, depature:datetime=None) -> None:
        if arrival is None:
            self.arrival = datetime.now()
        if depature is None:
            self.depature = datetime.now()

    def calculate_travel_time(self) -> datetime:
        time_diff = self.arrival - self.depature
        return (str(time_diff).split(":"))

    
    def get_wakeup_datetime(self, get_ready: time) -> datetime:
        ...

    def convert_string_to_time_object(time: str) -> time:
        (hour, minutes) = time.split(":")
        return time(hour=hour, minute=minutes)
