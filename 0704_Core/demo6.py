class Enemy:
    def __init__(self,atk):
        self.atk = atk
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        if 0 <= value <=100:
            self.__atk = value
        else:
            raise AtkError("错误",13,245,101)

class AtkError(Exception):
    def __init__(self,message,age_value,code_line,error_number):
        super().__init__("出错")
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_number

try:
    e01 = Enemy(110)
except AtkError as a:
    print(a.message)
    print(a.age_value)  
    print(a.code_line)
    print(a.error_number)