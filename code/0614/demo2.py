def fun_score(score):
    """
    :param:score 成绩

    :return:  级别
    """

    if score > 100 or score <0:
        return "false"
    elif 90 <= score:
        return "优秀"
    elif 80 <= score:
        return "良好"
    else:
        return "辣鸡"

re = fun_score(110)
print(re)