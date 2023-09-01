def total_number(*args):
    """
    :param 数值相加得函数
    :return:
    """
    result = 0
    for i in args:
        result += i
    return result
print(total_number(1,2,3,4))