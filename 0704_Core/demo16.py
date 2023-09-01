"""
    测试 通用模块list_helper
"""
from common.list_helper import ListHelper


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是:%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]

def condition01(item):
    return item.atk_ratio > 6


def condition02(item):
    return 4 < item.duration < 11


def condition03(item):
    return len(item.name) > 4 and item.duration < 6
generate01 = ListHelper.find_all(list_skill, condition01)
for item in generate01:
    print(item)

def condition04(item):
    return item.name == "葵花宝典"
def condition05(item):
    return item.id == 101
def condition06(item):
    return item.duration > 0

re = ListHelper.find_single(list_skill,condition05)
print(re)

re = generate02 = ListHelper.find_single(list_skill,lambda a: a.id == 101)
print(re)