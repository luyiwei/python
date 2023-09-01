"""
自定义线程类
"""
from threading import Thread

#自定义线程类(继承系统得父类)
class ThreadClass(Thread):
    #重写父类init
    def __init__(self,*args,**kwargs):
        self.attr = args[0]
        super().__init__() #加载父类init
    #假设需要很多步骤完成功能
    def f1(self):
        print("1111")
    def f2(self):
        print("22222")
    #重写run 逻辑调用
    def run(self):
        self.f1()
        self.f2()

t = ThreadClass('abc')
t.start() #自动运行run方法
t.join()