list_ache = []
while True:
    str_input = input("输入:")
    if str_input == "":
        break
    list_ache.append(int(str_input))
for i in list_ache:
    print(i)
print("最高："+str(max(list_ache)))
print("最低:" +str(min(list_ache)))
print("平均:" +str(sum(list_ache) / len(list_ache)))
