list01 = [3,4,55,6,7]
def my_enumerate(interable_target):
    index = 0
    for i in interable_target:
        yield (index,i)
        index +=1
for a,b in my_enumerate(list01):
    print(a,b)


list02 = ["孙悟空","猪八戒","唐僧","沙僧"]
list03 = [101,102,103,104]

def my_zip(list01,list02):
    for i in range(len(list01)):
        yield (list01[i],list02[i])
for i in my_zip(list02,list03):
    print(i)
