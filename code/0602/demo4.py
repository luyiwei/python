# score = int(input("成绩："))
count = 0
while count < 3:
    str_score = input("成绩：")
    if str_score == "":
        break
    score = int(str_score)
    if score > 100 or score < 0:
        count += 1
        print("错误")
    elif score > 80:
        print("好")
    else:
        print("不好")
else:
    print("错3次")

