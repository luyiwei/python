class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        # self.__hp = hp
        self.set_hp(hp)
        # self.__atk = atk
        self.set_atk(atk)
    def get_hp(self):
        return self.__hp
    def set_hp(self,value):
        if 50 < value < 100:
            self.__hp = value
        else:
            raise ValueError
    def get_atk(self):
        return self.__atk
    def set_atk(self,value):
        if 10 < value < 50:
            self.__atk = value
        else:
            raise ValueError
re = Enemy("aa",60,30)
print(re.get_hp())
print(re.get_atk())
re02 = Enemy("bb",70,40)
print(re02.get_hp())
print(re02.get_atk())