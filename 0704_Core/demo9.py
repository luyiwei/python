class Graphic:
    pass

class GraphicManger:
    def __init__(self):
        self.__graphics = []
    def add_graphic(self,graphic):
        self.__graphics.append(graphic)
    def __iter__(self):
        return GraphicIterator(self.__graphics)

class GraphicIterator:
    def __init__(self,target):
        self.__target = target
        self.__index = 0
    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp

manager = GraphicManger()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
for item in manager:
    print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except Exception:
        break