class Car():
    """Creating a car"""

    def __init__(self, model, year, engine, price):
        """Initialization the car's parameters"""
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.weels = 4

    def car_description(self):
        """Describing all parameters"""
        description = "Car model: " + str(self.model) + "\nProduction year: " + str(self.year) + "\nEngine capacity: " + str(self.engine) + " litres" + "\nPrice: " + str(self.price) + " rubles" + "\nOther paraneters: " + str(self.weels)
        return description

class Truck(Car):
    """Creating sub class"""

    def __init__(self, model, year, engine, price):
        super().__init__(model, year, engine, price)
        self.weels = 8

car = Car("VAZ 2106", 1991, 1.2, 30000)
print(car.car_description())
truck = Truck("KamAZ", 1988, 0.5, 400000)
print(truck.car_description())