import unittest

from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear_sensors = [1, 1, 0.2, 1]

        tires = OctoprimeTires(wear_sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear_sensors = [0.3, 0.1, 0.2, 0.7]

        tires = OctoprimeTires(wear_sensors)
        self.assertFalse(tires.needs_service())