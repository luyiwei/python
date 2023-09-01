# a = input("输入:")
# if a[::] == a[::-1]:
#     print(a)
# else:
#     print("not")
a = 100
b = 0
c = 100
# while True:
#     a /= 2
#     if a < 0.01:
#        break
#     else:
#         c += a
# print(c)
while a / 2 > 0.01:
    b += 1
    a /= 2
    c += a * 2
print("谈起%d次,"%(b))
print("距离是%.2f"%(c))



