from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self,wear_sensors) -> None:
        self.wear_sensors = wear_sensors
    
    def needs_service(self) -> bool:
        sum = 0
        for val in self.wear_sensors:
            sum+=val
        if sum >= 3:
            return True
        return False