"""
使用udp客户端查询单词，得到单词的解释
如果没有该单词则得到“没有单词”，客户端可以循环输入单词，直到输入空退出
服务端提供逻辑喝数据处理
客户端发送请求结果
"""
from socket import *
def find_word(word):
    f = open('dict.txt')
    for line in f:
        w = line.split(' ')[0]
        #如果遍历到的单词已经大于word就结束查找
        if w > word:
            f.close()
            return "没有单词"
        elif w == word:
            f.close()
            return line
    else:
        f.close()
        return "没有单词"

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
#绑定地址
server_addr = ('0.0.0.0',8888)
sockfd.bind(server_addr)

#循环收发消息
while True:
    #data接收到的单词
    data,addr = sockfd.recvfrom(1024)
    #查询单词解释
    result = find_word(data.decode())
    sockfd.sendto(result.encode(),addr)

#关闭套接字

sockfd.close()