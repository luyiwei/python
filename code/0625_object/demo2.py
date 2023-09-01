class Student:
    def __init__(self,name,age,score,sex):
        self. name = name
        self.age = age
        self.score = score
        self.sex = sex
    def print_self_info(self):
        print("%s的年龄是%d,成绩是%d,性别是%s" %(self.name,self.age,self.score,self.sex))
list01 = [
    Student("aa",28,100,"女"),
    Student("bb",68,62,"男"),
    Student("cc",30,95,"女"),
    Student("dd",28,70,"男"),
    Student("ee",28,70,"男"),
]
def find_name():
    """
    :param
    :return:
    """
    for item in list01:
        if item.name == "bb":
            return item
stu = find_name()
print(stu.name , stu.age)

def find_sex():
    """
    :param
    :return:
    """

    list02 = []
    for item in list01:
        if item.sex == "女":
           list02.append(item)
    return list02
re = find_sex()
for i in re:
    i.print_self_info()

def fun03():
    count = 0
    for item in list01:
        if item.age >= 30:
            count +=1
    return count

print(fun03())

def set01():
    for i in list01:
        i.score = 0
set01()
for i in list01:
    print(i.score)