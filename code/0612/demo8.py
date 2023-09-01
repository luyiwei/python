list01=[3,80,45,5,7,1]
for i in range(len(list01) - 1):
    for j in range(i+1,len(list01)):
        if list01[i] > list01[j]:
            list01[i],list01[j] = list01[j],list01[i]
print(list01)