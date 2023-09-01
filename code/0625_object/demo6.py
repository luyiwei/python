class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    def get_hp(self):
        return self.__hp
    def set_hp(self,value):
        if 50 < value < 100:
            self.__hp = value
        else:
            raise ValueError
    hp = property(get_hp,set_hp)
    def get_atk(self):
        return self.__atk
    def set_atk(self,value):
        if 10 < value < 50:
            self.__atk = value
        else:
            raise ValueError
    atk = property(get_atk,set_atk)
re = Enemy("aa",60,30)
print(re.atk,re.hp)
re02 = Enemy("bb",70,40)
print(re02.atk,re02.hp)