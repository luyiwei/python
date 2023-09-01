"""
基于协程的tcp并发
1.将每个客户端的处理设置为协程函数
2.让socket模块下的阻塞可以除非协程跳转
"""
import gevent
from gevent import monkey
monkey.patch_all() #执行脚本，修改socke阻塞
from socket import *


def handle(c):
    while True:
        data = c.recv(1024).decode
        if not data:
            break
        print(data)
        c.send(b'ok')

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

#循环接收客户端连接
while True:
    c,addr = s.accept()
    print("connect",addr)
    # handle(c) #处理具体客户端请求
    gevent.spwan(handle,c) #协程方案