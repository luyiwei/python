from common.list_helper import *
class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d"%(self.name,self.hp,self.atk,self.defense)
    def print_self_info(self):
        print(self.name,self.hp,self.atk,self.defense)


list01 = [
    Enemy("玄冥二老",86,120,58),
    Enemy("成昆",0,100,5),
    Enemy("谢逊",120,130,60),
    Enemy("灭霸",0,1309,690),
]
e = Enemy("玄冥二老",86,120,58)
e.print_self_info()
print(e)

re = ListHelper.find_single(list01,lambda item:item.name == "灭霸")
print(re)
re = ListHelper.find_all(list01,lambda element:element.atk > 10)
for i in re:
    print(i)

