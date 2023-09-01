def list_up(list01):
    """
    :param:
    :return:
    """
    for r in range(len(list01) - 1):
        for c in range(r+1,len(list01)):
            if list01[r] > list01[c]:
                list01[r],list01[c] = list01[c],list01[r]

list01 = [2,89,3,9,5]
list_up(list01)
print(list01)

