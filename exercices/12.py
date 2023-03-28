#Create a Bus class that inherits all methods and attributes from the Vehicle class
#below.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_vel = max_speed
        self.mileage = mileage



class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity