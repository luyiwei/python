from socket import *
import json
from config import *
from select import select
#应用类，出来某一方面的请求
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd.bind((frame_ip,frame_port))
    #启动服务
    def start(self):
        self.sockfd.listen(5)
        print("start %s"%frame_port)
        self.rlist.append(self.sockfd)
        #select 监控请求
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    self.handle(r)
                    self.rlist.remove(r)

    #处理具体的httpserver请求
    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        #request => {'methon':'GET','info':'/'}
        if request['method'] == 'GET':
            if request['info'] == '/' or \
                request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = {'status': '200', 'data': 'xxxxxx'}
        elif request['method'] == 'POST':
            pass
        #将数据发送给httpserver
        #response=>{'status': '200', 'data': 'xxxxxx'}
        response = json.dumps(response)

        connfd.send(response.encode())
        connfd.close()

    #处理网页
    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIR + "index.html"
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except Exception as e:
            fd = open(STATIC_DIR+'404.html')
            return {'status': '404', 'data': fd.read()}
        else:
            return {'status': '200', 'data': fd.read()}
app = Application()
app.start() #启动服务






