class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk =atk
        self.defense = defense
    def __str__(self):
        return "%s--%d--%d--%d"%(self.name,self.hp,self.atk,self.defense)
    def __repr__(self):
        return "Enemy('%s',%d,%d,%d)"%(self.name,self.hp,self.atk,self.defense)
e01 = Enemy("aa",100,10,5)
print(e01)

e02 = eval(repr(e01))
e02.name = "cc"
print(e02)
