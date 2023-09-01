"""
tcp客户端
"""
from socket import *
#创建tcp套接字
sockfd = socket() #使用默认擦书---》tcp套接字
#连接服务器
server_addr = ('127.0.0.1',8888) #服务器地址
sockfd.connect(server_addr)

#发送消息
data = input("Msg>>")
sockfd.send(data.encode()) #python传输中必须用字节串 不能用字符串 因为data是变量所以不能用b 只能用encode
data = sockfd.recv(1024)
print("Server:",data.decode()) #打印接收内容
#关闭套接字
sockfd.close()


