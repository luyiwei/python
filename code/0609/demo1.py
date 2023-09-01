tuple01 = (31,28,31,30,31,30,31,31,30,31,30,31)
moon = int(input("输入月份:"))
a = int(input("输入日期:"))
b = 0
if moon > 12 or moon <= 0 or a > 31 or a < 0:
    print("错误")
    exit("9")
for i in range(moon - 1 ):
    b += (tuple01)[i]
print(b+a)
# 
b = sum(tuple01[:moon - 1])
b += a