def fun_add(number):
    """
    :param: number:数字
    :return:
    """
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result
re=fun_add(1245)
print(re)