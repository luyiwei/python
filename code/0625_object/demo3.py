"""
4. 定义敌人类
    --　数据:姓名,血量,基础攻击力,防御力
    --　行为:打印个人信息

   创建敌人列表(至少４个元素),并画出内存图。
   查找姓名是"灭霸"的敌人对象
   查找所有死亡的敌人
   计算所有敌人的平均攻击力
   删除防御力小于10的敌人
   将所有敌人攻击力增加50
"""

class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
    def print_self_info(self):
        print(self.name,self.hp,self.atk,self.defense)
list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]
def find01():
    for i in list01:
        if i.name == "灭霸":
            return i
e01 =  find01()
if e01:
    e01.print_self_info()
else:
    print("无")

def find02():
    list_result = []
    for i in list01:
        if i.hp ==0:
            list_result.append(i)
    return list_result
re = find02()
for i in re:
    i.print_self_info()

def calculate01():
    sum_atk = 0
    for i in list01:
        sum_atk += i.atk
    return sum_atk / len(list01)
re = calculate01()
print(re)

def delete01():
    for i in range(len(list01) -1,-1,-1):
        if list01[i].defense < 10:
            del list01[i]
delete01()
for i in list01:
    i.print_self_info()

def set01():
    for i in list01:
        i.atk += 50
set01()
for i in list01:
    i.print_self_info()
