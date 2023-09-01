class StudentModel:
    def __init__(self,name = "",age = 0,score = 0,id = 0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score



class StudentManagerController:
    __init_id = 1000
    def __init__(self):
        self.__stu_list = []
    @property
    def stu_list(self):
        return self.__stu_list
    def add_student(self,stu_info):
        """
        添加一个学生
        :param stu_info: 没有编号的学生信息
        :return:
        """
        stu_info.id = self.__generate_id()
        self.stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self,id):
        for item in self.__stu_list:
            if item.id == id:
                 self.__stu_list.remove(item)
                 return True
            return False
    def update_student(self,stu_info):
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return  True
        return False

    def order_by_score(self):
       for r in range(len(self.__stu_list) - 1):
           for c in range(r + 1,len(self.__stu_list)):
               if self.__stu_list[r].score > self.__stu_list[c].score:
                   self.__stu_list[r],self.__stu_list[c] = self.__stu_list[c],self.__stu_list[r]

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
view = StudentManagerView().main()
# manager = StudentManagerController()
# s01 = StudentModel(2000,"zs",23,100)
# s02 = StudentModel(2000,"as",26,100)
# manager.add_student(s01)
# manager.add_student(s02)
# for i in manager.stu_list:
#     print(i.name,i.id)
# print(manager.remove_student(1001))
# for i in manager.stu_list:
#     print(i.name,i.id)
# manager.update_student(StudentModel(1002,"ts",29,100))
# for i in manager.stu_list:
#     print(i.name,i.id)