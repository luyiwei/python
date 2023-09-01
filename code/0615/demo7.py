def is_prim(i):
    """
    :param i:
    :return:
    """
    for item in range(2, i):
        if i % item == 0:
            return False
    return True


def get_prim(begin, end):
    """
    :param begin:
    :param end:
    :return:
    """
    list01 = []
    # for i in range(begin, end):
    #     if is_prim(i):
    #         list01.append(i)
    # return list01
    return [i for i in range(begin, end)if is_prim(i)]



print(get_prim(5,30))