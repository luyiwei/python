list01 = [9,25,12,8,26]
for i in range(len(list01)-1,-0,-1):
    print(i)
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)
