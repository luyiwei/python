import time

def verify_account(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execute_time = time.time() - start_time
        print("执行时间是:", execute_time)
        return result
    return wrapper
@verify_account
def fun01():
    time.sleep(2)
    print("fun01执行完毕了")
@verify_account
def fun02(a):
    time.sleep(1)
    print("fun02执行完毕",a)

fun01()
fun02(100)