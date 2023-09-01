from socket import *
from threading import Thread
import sys

#全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#设置套接字端口可立即重用
s.bind(ADDR)
s.listen(5)
print("Listen 8888")

while True:
    try:
        c,addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        sys.exit("推出服务器")
    except Exception as e:
        print(e)
        continue
 #创建线程处理请求
    t = Thread(target= handle,args=(c,))
    t.setDaemon(True)
    t.start()