from socket import *
import struct
#数据格式定义
st = struct.Struct('i32sif')
ADDR = ('127.0.0.1',9999)
#udp套接字
s = socket(AF_INET,SOCK_DGRAM)

while True:
    print("=============================")
    id = int(input(("ID:")))
    name = input('Name:').encode()
    age = int(input("Age:"))
    score = float(input("Score:"))
    #打包数据发送
    data = st.pack(id,name,age,score)
    s.sendto(data,ADDR)