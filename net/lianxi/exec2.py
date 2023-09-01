"""
创建2个进程
分别复制文件得上半部分和下半部分到一个新的文件中
"""
from multiprocessing import Process
import os
filename = './face,jpg'
size = os.path.getsize(filename)

#复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

#复制下半部分
def bot():
    fr = open(filename,'rb')
    fw = open('bop.jpg','wb')
    #移动偏移量
    fr.seek(size // 2,0) #以开头为基准向后移动除以2得字节
    fw.write(fr.read()) #read()什么也不写默认读到结尾
    fr.close()
    fw.close()

p1 = Process(target= top)
p2 = Process(target= bot)
p1.start()
p2.start()
p1.join()
p2.join()