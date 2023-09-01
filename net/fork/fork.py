"""
fork进程创建演示
"""
import os
pid = os.fork()

if pid < 0:
    print("faild")
#子进程执行部分
elif pid == 0:
    print("new")
#父进程执行部分
else:
    print("old")
#共同执行部分
print("Fork test over")