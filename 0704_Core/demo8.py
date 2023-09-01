class Skill:
    pass
class SkillManager:
    """
        技能管理器  可迭代对象
    """
    def __init__(self):
        self.__skills = []
    def add_skill(self,skill):
        self.__skills.append(skill)

    def __iter__(self):
        return SkillIterator(self.__skills)

class SkillIterator:
    """
        技能迭代器
    """
    def __init__(self,target):
        self.__target = target
        self.__index = 0
    def __next__(self):
        if self.__index > len(self.__target) -1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index +=1
        return temp


manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

for item in manager:
    print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break