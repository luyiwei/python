class Car:
    def __init__(self,brand,speed):
        self.speed = speed
        self.brand = brand



class Electric(Car):
    def __init__(self,speed,brand,capacity,power):
        super().__init__(speed,brand)
        self.capacity = capacity
        self.power = power

# car = Car("奔驰",230)
# electric = Electric("aa",120,150,220)


