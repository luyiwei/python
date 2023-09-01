list01 = [43,4,5,5,6,7,87]
def find01():
    for item in list01:
        if item % 2 == 0:
            yield item
def find02():
    for item in list01:
        if item > 10:
            yield item
def find03():
    for item in list01:
        if 10 < item < 50:
            yield item

def condition01(item):
    return item % 2 == 0

def condition02(item):
    return item > 10

def condition03(item):
    return  10 < item < 50

def find(func_condition):
    for i in list01:
        if func_condition(i):
            yield i
for item in find(condition02):
    print(item)