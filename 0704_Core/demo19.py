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
    Enemy("成昆",0,100,5),
    Enemy("谢逊",120,130,60),
    Enemy("灭霸",0,1309,690),
]
re = ListHelper.find_sum(list01,lambda item:item.atk)
print(re)
re = ListHelper.find_all(list01,lambda item:(item.name,item.hp))
print(re)
re = ListHelper.find_select(list01,lambda item:(item.name,item.hp))
for item in re:
    print(item)

re = ListHelper.get_max(list01,lambda item:item.hp)
print(re)

re = ListHelper.get_up(list01,lambda item:item.hp)

for item in list01:
    print(item)