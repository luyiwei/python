"""

"""
from test import *
import time
from multiprocessing import Process

jobs = []
tm = time.time()
for i in range(10):
    p = Process(target=count,args=(1,1))
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()

print(time.time() - tm)