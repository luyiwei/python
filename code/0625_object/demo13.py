class Grenade:
    def __init__(self,atk):
        self.atk = atk
    def explode(self,damage_target):
        if not isinstance(damage_target,Damageable):
            raise ValueError("不是Damageable的子类")
        print("炸了")
        damage_target.damage(self.atk)

class Damageable:
    def damage(self,value):
        raise NotImplementedError()

class Player(Damageable):
    def __init__(self,hp):
        self.hp = hp
    def damage(self,value):
        self.hp -= value
        print("玩家受伤")
        print("碎屏")
        print(self.hp)
class Enemy(Damageable):
    def __init__(self,hp):
        self.hp = hp
    def damage(self,value):
        self.hp -= value
        print("敌人受伤")
        print("豹子")

g01 = Grenade(100)
e01 = Enemy(200)
p01 = Player(300)
g01.explode(p01)



