import unittest
from datetime import datetime

from batteries.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    # True if last service date and current date's diff is 2 years (service 2 years once)
    # Task 4 - Update, 3 years
    def test_needs_service_true(self):
        # last_service_date = datetime(2020, 5, 17)
        last_service_date = datetime(2019, 5, 17)
        current_date = datetime(2022,5,17)
        battery = SpindlerBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())
        

    def test_needs_service_false(self):
        last_service_date = datetime(2021, 5, 17)
        current_date = datetime(2022,5,17)
        battery = SpindlerBattery(last_service_date,current_date)
        self.assertFalse(battery.needs_service())
