class Persion:
    def __init__(self,name,):
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)

    def work(self,money):
        print(self.name,"上班挣了%d"%money)
zwj = Persion("张无忌")
zm = Persion("赵敏")
zwj.teach(zm,"aa")
zwj.work(10000)



