from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

#接收文件思路：    1.wb打开新文件
#               2. rece 内容 write文件
#打开文件
f = open('gg.jpg','wb')
# 循环接收写入文件
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)
f.close()
c.close()
s.close()
