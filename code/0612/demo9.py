result = False
list01 = [3,80,45,5,81,1]
for i in range(len(list01) - 1):
    for j in range(i+1,len(list01)):
        if list01[i] == list01[j]:
            print("有相同项：" +str(list01[i]))
            # list01.remove(list01[j])
            result = True
if result == False:
    print("没有相同项")