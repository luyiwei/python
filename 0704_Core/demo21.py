from common.list_helper import *
class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d"%(self.name,self.hp,self.atk,self.defense)
list01 = [
    Enemy("玄冥二老",86,120,58),
    Enemy("成昆",0,100,555),
    Enemy("谢逊",120,130,60),
    Enemy("灭霸",0,1309,690),
]
re = ListHelper.get_min(list01,lambda item:item.defense)
print(re)

re = ListHelper.order_by_descending(list01,lambda item:item.defense)
for i in list01:
    print(i)