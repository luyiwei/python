from socket import *
# 客户端（浏览器）处理
def request(connfd):
    # 获取请求将请求内容提出来
    data = connfd.recv(4096) #接收请求
    #防止浏览器异常退出
    if not data:
        return
    request_line = data.decode().split('\n')[0]
    info = request_line.split(' ')[1]
    #判断是/ 返回index.html 不是返回404
    if info == '/':
        with open('index.html') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "sorry"
    # 发送给浏览器
    connfd.send(response.encode())

sockfd = socket()
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(3)
while True:
    connfd,addr = sockfd.accept()
    request(connfd) #处理客户端请求
