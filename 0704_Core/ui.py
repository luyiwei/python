from  bll import StudentManagerController
from model import *
class StudentManagerView:
    """
          界面视图类
    """
    def __init__(self):
        self.__manger = StudentManagerController()
    def __display_menu(self):
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩升序排列")

    def __select_menu(self):
        item = input("请输入:")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student(self.__manger.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("姓名")
        age = int(input("年龄"))
        score = int(input("分数"))
        stu = StudentModel(name,age,score)
        self.__manger.add_student(stu)

    def __output_student(self,list_output):
        for item in list_output:
            print(item.id,item.age,item.score,item.name)

    def __delete_student(self):
        id = int(input("id号:"))
        if self.__manger.remove_student(id):
            print("成功")
        else:
            print("失败")

    def __modify_student(self):
        id = int(input("id号:"))
        name = input("新姓名")
        age = int(input("新年龄"))
        score = int(input("新分数"))
        stu = StudentModel(name,age,score,id)
        if self.__manger.update_student(stu):
            print("成功")
        else:
            print("失败")

    def __output_student_by_score(self):
        self.__manger.order_by_score()
        self.__output_student(self.__manger.stu_list)