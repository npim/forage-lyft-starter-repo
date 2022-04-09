import unittest
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    # Should be serviced once every 4 years
    def test_needs_service_true(self):
        last_service_date = datetime(2018, 5, 17)
        current_date = datetime(2022,5,17)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime(2020, 5, 17)
        current_date = datetime(2022,5,17)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertFalse(battery.needs_service())