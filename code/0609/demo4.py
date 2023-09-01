dict_info = {}
while True:
    name = input("姓名:")
    if name == "":
        break
    age = int(input("年龄:"))
    achie = int(input("成绩:"))
    sex = input("性别:")
    dict_info[name] = {"age":age,"achie":achie,"sex":sex}
for k,v in dict_info.items():
    print("%s的年龄是%d,成绩是%d,性别是%s"%(k,v["age"],v["achie"],v["sex"]))