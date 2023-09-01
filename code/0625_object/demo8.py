class Person:
    def __init__(self,name,money):
        self.name = name
        self.money = money
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):
        self.__money = value


class Bank:
    def __init__(self,name,money):
        self.name = name
        self.money = money
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    def draw_money(self,person,value):
        self.money -= value
        person.money = +value
        print(person.name,self.name,"取%d钱"%value)

xm = Person("小明",0)
zsyh = Bank("招商",2000)
zsyh.draw_money(xm,1000)