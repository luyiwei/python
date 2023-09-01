"""
2048 游戏核心算法
"""
# list_merge = [2,0,4,4]
def zero_to_end(list_merge):
    """
    零元素引动到末尾
    思想：重后向前，发现零删除，并在末尾追加
    :return:
    """
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)
list_merge = [2, 0, 4, 4]
zero_to_end(list_merge)
print(list_merge)


def merge(list_merge):
    zero_to_end(list_merge)
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] *=2
            del list_merge[i+1]
            list_merge.append(0)
list_merge = [2,2,4,6]
merge(list_merge)
print(list_merge)
# 地图向左移动

def map_left_move(map):
    for i in range(len(map)):
        merge(map[i])
map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
map_left_move(map)
print(map)


