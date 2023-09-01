"""
io多路复用和http
"""
from socket import *
from select import *
#具体功能实现
class HTTOServer:
    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host,port)
        #多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        #实例化对象时调用函数直接创建套接字
        self.create_socket()
        self.bind()
    #创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    #绑定地址
    def bind(self):
        # self.sockfd.bind(self.address)
        self.sockfd.bind(('0.0.0.0',8000))

    #启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("lister the port %d"%self.port)
        #IO多路复用接收客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs,wx,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c,addr = r.accept()
                    # print("connect",addr)
                    self.rlist.append(c)
                else:
                    # print(r.recv(4096))
                    #处理请求
                    self.handle(r)
    def handle(self,connfd):
        #接收http请求
        request = connfd.recv(4096)
        #客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        #提取请求内容
        request_line = request.splitlines()[0]  #splitlines将字节串按行切割
        info = request_line.decode().split(' ')[1]
        print(connfd.getpeername(),':',info) #获取连接的客户端地址
        #根据请求内容进行数据整理
        #分为两类，1.请求网页 2.其他
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd,info)
        else:
            self.get_data(connfd,info)
    #返回网页
    def get_html(self,connfd,info):
        if info == '/':
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            #网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "sorry"
        else:
            #网页存在
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += fd.read()
        # finally:
        #     #将响应发送给浏览器
        #     connfd.send(response.encode())
        connfd.send(response.encode())

    #其他数据
    def get_data(self,connfd,info):
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "waiting........"
            response += "sorry"
            connfd.send(response.encode())

#用户使用httpserver
if __name__=="__main__":
    """
    通过httpserver类快书搭建服务
    """
    #用户决定的参数
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = './static' #网页存储位置
    httpd = HTTOServer(HOST,PORT,DIR)  #实例化服务
    httpd.serve_forever() #启动服务

