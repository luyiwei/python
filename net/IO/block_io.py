"""
socket 套接字非阻塞示例
"""
from socket import *
from time import ctime,sleep

#打开一个日志文件
f = open('lgo.txt','a+')
#tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(3)
#设置套接字为非阻塞
sockfd.setblocking(False)
while True:
    print("waiting....")
    #没有客户端连接每隔3秒写一条日志
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError as e:
        sleep(3)
        f.write("%s : %s\n"%(ctime(),e))
        f.flush()
    else:
        print("connect from",addr)
        data = connfd.recv(1024).decode() #虽然把sockfd设置成了非阻塞但recv还是阻塞的，要相recv变成非阻塞 就需要把掉用他的对象设置成非阻塞，也就是把connfd设置成非阻塞
        print(data)