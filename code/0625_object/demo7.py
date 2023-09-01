class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        if 50 < value < 100:
            self.__hp = value
        else:
            raise ValueError("cuowu")
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        if 10 < value < 50:
            self.__atk = value
        else:
            raise ValueError("sdsdsdf")
re = Enemy("aa",60,30)
print(re.atk,re.hp)
re02 = Enemy("bb",70,40)
print(re02.atk,re02.hp)