import unittest
from datetime import datetime

from engines.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    # Should be serviced once every 30,000 miles
    def test_needs_service_true(self):
        last_service_mileage = 30000
        current_mileage = 60000
        engine = CapuletEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_service_mileage = 30000
        current_mileage = 35000
        engine = CapuletEngine(last_service_mileage,current_mileage)
        self.assertFalse(engine.needs_service())