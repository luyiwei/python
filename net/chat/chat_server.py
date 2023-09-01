from socket import *
import os,sys
"""
全局变量:一般全用大写
"""
#服务器地址
ADDR = ('0.0.0.0',8889)
#存储用户 {name:address}
user = {}

#登录
def do_login(s,name,addr):
    if name in user:
        s.sendto('该用户存在'.encode(),addr)
        return
    s.sendto(b'OK',addr) #可以进入聊天室
    # 通知其他人
    msg = "欢迎'%s'进入俩天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr # 插入字典

#聊天
def do_chat(s,name,text):
    msg = "%s: %s"%(name,text)
    for i in user:
        #刨除其本人
        if i != name:
            s.sendto(msg.encode(),user[i])

#退出
def do_quit(s,name):
    msg = "%s 退出聊天室"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[i])
    del user[name] #删除用户


# 处理请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ') #拆分请求
        #根据不同得请求类型 具体执行不通得事情
        # L 进入  C 聊天 Q 推出
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr) #执行具体工作
        elif tmp[0] == 'C':
            text = ' '.join(tmp[2:])
            do_chat(s,tmp[1],text)
        elif tmp[0] == 'Q':
            do_quit(s,tmp[1])
#搭建网络
def main():
    #udp服务端
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    # 请求处理函数
    do_request(s) #s是套接字

main()