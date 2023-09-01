"""
消息队列符合先进先出原则
"""
from multiprocessing import Queue,Process
from time import sleep
from random import randint
#创建消息队列
q = Queue(5) #最大长度5

def handle():
    for i in range(6):
        x = randint(1,34)
        q.put(x) #消息入队
    q.put(randint(1,16))

def request():
    while True:
        # print("..........")
        sleep(2)
        try:
            print(q.get(3),end=' ') #消息出队 3为超时时间
        except:
            break

p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()