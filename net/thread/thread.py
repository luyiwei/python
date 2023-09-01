"""
线程
基本步骤同Process
1.封装线程
2.创建线程对象
3.启动线程
4.回收线程
"""
import threading
from time import sleep
import os
#线程函数
def music():
    for i in range(3):
        sleep(2)
        print("播放:合唱")

#创建线程对象
t = threading.Thread(target= music)
t.start()#启动线程
for i in range(4):
    sleep(1)
    print("aaa")
t.join()#回收线程
#这个项目有2个线程 一个是start启动得主线程 一个是运行函数得副线程