from abc import ABC
from dateutil import relativedelta

from batteries.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
       self.last_service_date = last_service_date
       self.current_date = current_date

    def needs_service(self) -> bool:
        diff = relativedelta.relativedelta(self.current_date, self.last_service_date)
        if diff.years>=4:
            return True
        else:
            return False

