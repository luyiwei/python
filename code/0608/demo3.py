list_01 = ["-11","2","3","4","5"]
str_min = "3"
for i in range(0,len(list_01)):
    # if int(str_min) > int(list_01[i]):
    if str_min > list_01[i]:
        str_min = list_01[i]
print(str_min)

