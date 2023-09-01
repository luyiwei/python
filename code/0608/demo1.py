list_temp = []
while True:
    a = str(input("输入:"))
    if a == "":
        break
    list_temp.append(a)
str_result = "".join(list_temp)
print(str_result)