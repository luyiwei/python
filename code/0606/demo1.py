num = int(input("输入数字:"))
a = "*" * num
print(a)
for i in range(num-2):
    print("*" + " "*(num - 2) + "*")
print(a)