def get_same(list_name):
    """
    :param:list_name
    :return:
    """

    for i in range(len(list_name)):
        for j in range(i+1,len(list_name)):
            if list_name[i] == list_name[j]:
                return True
    return False
print(get_same([1,2,3,4]))