import unittest
# from datetime import datetime

from engines.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    # Should be serviced once every 60,000 miles
    def test_needs_service_true(self):
        last_service_mileage = 120000
        current_mileage = 180000
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_service_mileage = 120000
        current_mileage = 125000
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertFalse(engine.needs_service())