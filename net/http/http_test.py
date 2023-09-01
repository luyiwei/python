from socket import *
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(3)
c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096) #接受httpqingq
print(data)

response = """HTTP/1.1 200 OK
Content-Type:text/html

hello world
"""

c.send(response.encode())
c.close()