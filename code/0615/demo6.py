

def get_prim(begin,end):
    """

    :param begin:
    :param end:
    :return:
    """
    list01 = []
    for i in range(begin,end):
        for item in range(2,i):
            if i % item == 0:
                break
        else:
            list01.append(i)
    return list01
print(get_prim(5,30))