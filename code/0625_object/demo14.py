class GraphicManager:
    def __init__(self):
        self.__graphics = []
    def add_graphic(self,graphic):
        if isinstance(graphic,Graphic):
            self.__graphics.append(graphic)
        else:
            raise ValueError("no")
    def get_total_area(self):
        total_area = 0
        for item in self.__graphics:
            total_area += item.calculate_area()
        return  total_area

class Graphic:
    def calculate_area(self):
        pass


class Circular(Graphic):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return  3.14 * self.radius **2

class Rectangle(Graphic):
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
    def calculate_area(self):
        return self.lenght * self.width
c01 = Circular(5)
r01 = Rectangle(10,20)
manager = GraphicManager()
manager.add_graphic(c01)
manager.add_graphic(r01)
re = manager.get_total_area()
print(re)


