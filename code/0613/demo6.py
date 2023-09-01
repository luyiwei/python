def change_matrix(list01):
    """
    :param

    """
    for r in range(1, len(list01)):
        for c in range(r, len(list01)):
            list01[c][r - 1], list01[r - 1][c] = list01[r - 1][c], list01[c][r - 1]
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
change_matrix(list01)
print(list01)
change_matrix(list01)
print(list01)
print(list01)