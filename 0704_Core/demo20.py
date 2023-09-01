tuple01 = ([1,1,1],[2,2],[3,3,3,3])
re = max(tuple01,key = lambda item:len(item))
print(re)

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
map(lambda item:(item.name,item.hp,item.atk),list01)
for item in re:
    print(item)

re = filter(lambda item:item.atk>100 and item.hp>0,list01)
for item in re:
    print(item)

sorted(list01,key = lambda item:item.atk,reverse= True)
for item in re:
    print(item)