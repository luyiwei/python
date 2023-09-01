class StaffManager:
    def __init__(self):
        self.__list = []
    def add_staff(self,staff):
        if isinstance(staff,Staff):
            self.__list.append(staff)
        else:
            raise ValueError("no")
    def get_total_salary(self):
        total_salary = 0
        for item in self.__list:
            total_salary += item.salary()
        return total_salary

class Staff:
    def __init__(self,basic):
        self.basic = basic
    def salary(self):
        pass

class Programmer(Staff):
    def __init__(self,basic,bonus):
        super().__init__(basic)
        self.__bonus = bonus
    def salary(self):
        return  self.basic + self.__bonus

class Sale(Staff):
    def __init__(self,basic,volume):
        super().__init__(basic)
        self.__volume = volume
    def salary(self):
        return  self.basic + self.__volume * 0.05

a01 = StaffManager()
b01 = Programmer(100,200)
c01 = Sale(500,300)
a01.add_staff(b01)
a01.add_staff(c01)
re = a01.get_total_salary()
print(re)