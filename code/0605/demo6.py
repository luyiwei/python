# print(str(input("输入："))[0])
# print(str(input("输入："))[-1])
# print(str(input("输入："))[-3])
# print(str(input("输入："))[:2])
# print(str(input("输入："))[::-1])
num = str(input("输入："))
num_01 = len(num)
if num_01 % 2 != 0:
    print(num[num_01 // 2 ])
