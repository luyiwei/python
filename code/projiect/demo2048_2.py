"""
2048 游戏核心算法
"""
list_merge = [2,0,4,4]
def zero_to_end():
    """
    零元素引动到末尾
    思想：重后向前，发现零删除，并在末尾追加
    :return:
    """
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)
# zero_to_end()
# print(list_merge)


def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] *=2
            del list_merge[i+1]
            list_merge.append(0)
# merge()
# print(list_merge)
# 地图向左移动

def move_left():
    for line in map:
        global list_merge
        list_merge = line
        merge()
map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
# move_left()
# print(map)

def move_right():
    for line in map:
        global list_merge
        list_merge = line[::-1]
        merge()
        print(list_merge)
        line[::-1] = list_merge


# move_right()
# print(map)

def squre_matrix_transpose(sqr_matrix):
    for c in range(1,len(sqr_matrix)):
        for r in range(c,len(sqr_matrix)):
            sqr_matrix[r][c - 1],sqr_matrix[c - 1][r] = sqr_matrix[c - 1][r],sqr_matrix[r][c - 1]
def move_up():
    squre_matrix_transpose(map)
    move_left()
    squre_matrix_transpose(map)

def down_up():
    squre_matrix_transpose(map)
    move_right()
    squre_matrix_transpose(map)

# move_up()
# print(map)
down_up()
print(map)