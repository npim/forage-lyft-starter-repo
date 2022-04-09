from tires import Tires

class CarriganTires(Tires):
    def __init__(self,wear_sensors) -> None:
        self.wear_sensors = wear_sensors
    
    def needs_service(self) -> bool:
        for val in self.wear_sensors:
            if val>=0.9:
                return True
        return False