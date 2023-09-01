
# 练习:在控制台中录入多个人的多个喜好
# 例如: 请输入姓名 :##
# 请输入第1个喜好
# 请输入第2个喜好
# ######
# 请输入姓名 :
# 输入空字符停止
# 最后在控制台打印所有人的所有喜好

dict_name_hobby = {}
# list_hobby = []
while True:
    name = input("姓名:")
    if name == "":
        break
    # list_hobby = []
    dict_name_hobby[name] = []
    while True:
        hobby = input("喜好:")
        if hobby == "":
            break
        # list_hobby.append(hobby)
        dict_name_hobby[name].append(hobby)
    # dict_name_hobby[name] = list_hobby
print(dict_name_hobby)
for k,v in dict_name_hobby.items():
    print("%s喜欢,%s"%(k,v))