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