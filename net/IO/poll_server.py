"""
poll 完成tcp并发
IO多路复用实现并发
建立fileno----》 io对象字典用于io查找
1.创建套接字
2.将套接字register
3.创建查找字典，并文虎
4.循环监控io发生
5.处理发生的io
"""
from socket import *
from select import *
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)
#创建poll对象
p = poll()
#建立查找字典，通过一个io的fineno找到io对象
#一直和register的io保持一致
fdmap = {s.fileno():s}
#关注s
p.register(s,POLLIN|POLLERR)
#循环监控io发生
while True:
    events = p.poll()
    # print(events)
    #循环遍历列表，查看哪个io就绪，进行处理
    for fd,event in events:
        # print("fileno:",fd)
        # print("event:",event)
        #区分哪个io就绪
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('connect:',addr)
            #关注客户端连接套接字
            p.register(c,POLLIN|POLLERR)
            fdmap[c.fileno()] = c #维护字典
        elif event & POLLIN: #判断是否为POLLIN就绪
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd) #取消关注
                fdmap[fd].close()
                del fdmap[fd] #从字典删除
                continue
            print(data)
            fdmap[fd].send(b'ok')