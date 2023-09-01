class Player:
    def __init__(self,hp,atk):
        self.atk = atk
        self.hp = hp
    def attack(self,other):
        print("玩家攻击敌人")
        other.damage(self.atk)

    def damage(self,value):
        print("玩家受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家die")
        print("游戏结束")


class Enemy:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk
    def damage(self,value):
        self.hp -= value
        if self.hp <= 0:
            self.__death()
    def __death(self):
        print("die")
        print("lose")
        print("add")

    def attack(self,other):
        print("敌人攻击玩家")
        other.damage(self.atk)


p01 = Player(1000,100)
e01 = Enemy(200,10)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)