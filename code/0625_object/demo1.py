class Student:
    def __init__(self,name,age,score,sex):
        self. name = name
        self.age = age
        self.score = score
        self.sex = sex
    def print_self_info(self):
        print("%s的年龄是%d,成绩是%d,性别是%s" %(self.name,self.age,self.score,self.sex))

s01 = Student("赵敏",26,100,"女")
s01.print_self_info()
Student("赵敏",26,100,"女").print_self_info()