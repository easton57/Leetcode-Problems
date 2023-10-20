class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spots = [big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.spots[0] > 0:
            self.spots[0] -= 1
            return True
        elif carType == 2 and self.spots[1] > 0:
            self.spots[1] -= 1
            return True
        elif carType == 3 and self.spots[2] > 0:
            self.spots[2] -= 1
            return True

        return False
