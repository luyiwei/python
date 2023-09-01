list01 = []
for i in range(1970,2051):
    if i % 4 == 0 and i % 100 !=0 or i % 400 == 0 :
        # print(i)
        list01.append(i)
print(list01)
