"""
协程模块
"""
import gevent
#携程函数
def foo(a,b):
    print("running foo...",a,b)
    gevent.sleep(2)
    print("foo again..")

def bar():
    print("running foo...")
    gevent.sleep(3)
    print("bar again..")
#生成携程对象
f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)

gevent.joinall([f,b]) #阻塞等待f,b两个协程执行完毕