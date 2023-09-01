def core():
    while True:
        str_result = input("成绩:")
        try:
            score = int(str_result)
        except:
            print("必须输入整数")
            continue
        if 0 < score < 100:
            return score
        else:
            print("超过范围")
print(core())
