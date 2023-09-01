"""
tcp套接字服务端流程
"""
import socket
#创建tcp（流式）套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0',8888))
#设置监听
sockfd.listen(5)
#阻塞等待处理连接
print("wait for connect....")
connfd,addr = sockfd.accept()
print("Connect from",addr) # 打印链接得客户端地址

#收发消息
data = connfd.recv(1024)
print("收到:",data)
n = connfd.send(b'Thanks') #发送字节窜
print("发送%d字节"%n)

#关闭套接字
connfd.close()
sockfd.close()

