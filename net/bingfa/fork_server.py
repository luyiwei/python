"""
基于fork的多进程并发
创建监听套接字
等待接收客户端请求
客户端连接创建新的进程处理客户端请求
原进程继续等待其他客户端连接
如果客户端退出，则销毁对应的进程
"""
from multiprocessing import Process
from socket import *
import os
import signal

#全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
#具体处理客户端请求：
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

#创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#设置套接字端口可立即重用
s.bind(ADDR)
s.listen(5)
#处理僵尸进程（非阻塞）
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("Listen 8888")

while True:
    #循环处理客户端连接
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:#相当于ctrl-c
        os._exit(0)
    except Exception as e: #Execption 常规错误
        print(e)
        continue #忽略当前循环，进行下一次循环

    #创建子进程处理客户端事务
    pid = os.fork()
    if pid == 0:
        s.close() #对子进程来说s没用
        handle(c) #处理具体事务的函数（自己写的）
        os._exit(0) #子进程销毁
    #无论父进程还是fork出错都要回去继续处理连接
    else:
        c.close() #对父进程来说c无用，c已经传到了子进程里，而父进程就是不断的接收客户端的连接，不需要和任何客户端沟通 所以无用
 #####################################################
    #创建子进程处理客户端事务 (基于Process的方法)
    p = Process(target= handle,args=(c,))
    p.daemon = True #父进程退出，子进程也退出
    p.start()
