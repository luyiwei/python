def print_c(list_one):
    """
    :paramL:list_one 输入列表
    :return:
    """
    for i in range(len(list_one)):
        for j in range(len(list_one[i])):
            print(list_one[i][j],end=" ")
        print()
list01 = [[1,2,3],[4,5,6],[7,8]]
print_c(list01)