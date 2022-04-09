import datetime
from car import Car

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

class CarFactory:
    # def __init__(self):
    #     pass


    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        # Capulet Engine
        capulet = CapuletEngine(last_service_mileage,current_mileage)
        # Spindler Battery
        spindler = SpindlerBattery(last_service_date,current_date)

        calliope = Car(capulet,spindler)
        return calliope
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        # Willoughby Engine
        willoughby = WilloughbyEngine(last_service_mileage,current_mileage)
        # Spindler Battery
        spindler = SpindlerBattery(last_service_date,current_date)

        glissade = Car(willoughby,spindler)
        return glissade

    def create_palindrome(current_date, last_service_date, warning_light_on):
        # Sternman Engine
        sternman = SternmanEngine(warning_light_on)
        # Spindler Battery
        spindler = SpindlerBattery(last_service_date,current_date)

        palindrome = Car(sternman,spindler)
        return palindrome

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        # Willoughby Engine
        willoughby = WilloughbyEngine(last_service_mileage,current_mileage)
        # Nubbin Battery
        nubbin = NubbinBattery(last_service_date,current_date)

        rorschach = Car(willoughby,nubbin)
        return rorschach

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        # Capulet Engine
        capulet = CapuletEngine(last_service_mileage,current_mileage)
        # Nubbin Battery
        nubbin = NubbinBattery(last_service_date,current_date)
        
        thovex = Car(capulet,nubbin)
        return thovex
