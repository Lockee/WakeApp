from datetime import datetime, time


class TimeController:
    def __init__(self, arrival:datetime=None, depature:datetime=None, get_ready:time=None) -> None:
        if arrival is None:
            self.arrival = datetime.now()
        if depature is None:
            self.depature = datetime.now()
        if get_ready is None:
            self.get_ready = time(hour=0,minute=30,second=0)

    def calculate_travel_time(self) -> time:
        ...

    
    def get_wakeup_datetime(self) -> datetime:
        ...
