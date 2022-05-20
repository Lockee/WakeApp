from datetime import datetime, time


class TimeController:
    def __init__(self, arrival:datetime=None, depature:datetime=None) -> None:
        if arrival is None:
            self.arrival = datetime.now()
        if depature is None:
            self.depature = datetime.now()

    def calculate_travel_time(self) -> time:
        ...

    
    def get_wakeup_datetime(self, get_ready: time) -> datetime:
        ...
