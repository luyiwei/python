list_name = []
while True:
    str_name = input("名字:")
    if str_name == "":
        break
    if str_name in list_name:
        print("存在")
    else:
        list_name.append(str_name)
# print(list_name[::-1])
# for i in range(-1,-len(list_name)-1,-1):
#     print(list_name[i])
for i in range(len(list_name) - 1, - 1,-1):
    print(list_name[i])