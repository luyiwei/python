list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
# print(list01[1][2])
# list02 = list01[2]
# for i in range(len(list02)):
#     print(list02[i])
#
# for r in range(len(list01)):
#     print(list01[r][0])
list02 = []
for r in range(len(list01)):
    list02.append([])
    for c in range(4):
        list02[r].append(list01[c][r])
print(list02)