"""
多线程并发
tcp传输
将基本文件操作封装为类
协议确定
L请求查看文件列表
Q退出
G下载
p上传
"""
import sys
import time
from threading import Thread
from socket import *
import os
#全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
FTP = "/home/tarena/FTP/" #文件库位置


#创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
    查看，下载，上传，退出
    """
    def __init__(self,confd):
        self.confd = confd
        super().__init__()
    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.confd.send("文件库为空".encode())
            return
        else:
            self.confd.send(b'ok')
            time.sleep(0.1)
        #拼接文件
        filelist = ""
        for file in files:
            if file[0] !='.' and os.path.isfile(FTP+file):
                filelist += file + '\n'
        self.confd.send(filelist.encode())

    def do_get(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except Exception: #打开失败文件不存在
            self.confd.send('文件不存在'.encode())
            return
        else:
            self.confd.send(b'OK')
            time.sleep(0.1)
        #发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.confd.send(b'##') #发送完成
                break
            self.confd.send(data)

    def do_put(self,filename):
        if os.path.exists(FTP + filename):
            self.confd.send("文件存在")
            return
        else:
            self.confd.send(b'OK')
        #接收文件
        f = open(FTP+filename,'wb')
        while True:
            data = self.confd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()
    #循环接收请求，分情况调用功能函数
    def run(self):
        while True:
            data = self.confd.recv(1024).decode()
            if not data or data == 'Q':
                return #线程结束
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)


#搭建网络服务器端模型
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置套接字端口可立即重用
    s.bind(ADDR)
    s.listen(5)

    print("listen the port 8888....")
    while True:
        try:
            c,addr = s.accept()
            print("Connect from", addr)
        except Exception as e:
            print(e)
            continue
        except KeyboardInterrupt:
            sys.exit("推出服务器")
        client = FTPServer(c)
        client.setDaemon(True)
        client.start() #运行run


if __name__ == "__main__":
    main()