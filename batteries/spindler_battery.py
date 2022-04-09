from abc import ABC
from dateutil import relativedelta

from batteries.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
       self.last_service_date = last_service_date
       self.current_date = current_date

    def needs_service(self) -> bool:
        diff = relativedelta.relativedelta(self.current_date, self.last_service_date)
        # Previously after 2 years (Task 1-3)
        if diff.years>=3:
            return True
        else:
            return False

