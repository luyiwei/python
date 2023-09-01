from test import *
import time
from threading import Thread

jobs = []
tm = time.time()
for i in range(10):
    t = Thread(target=count,args=(1,1))
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()

print(time.time() - tm)