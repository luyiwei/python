"""
线程互斥方法
"""
from  threading import Thread,Event

s = None #用于通信
e = Event()#事件对象

def aaa():
    print("山头")
    global s
    s = "天王"
    e.set() #操作完共享资源 e 设置

t = Thread(target=aaa)
t.start()

print("说对自己人")
e.wait() #阻塞等待
if s == '天王':
    print("dui")
else:
    print("no")

t.join()