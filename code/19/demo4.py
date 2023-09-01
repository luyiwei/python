num1 = float(input("第一个:"))
num2 = float(input("第二个"))
num3 = float(input("第三个"))
num4 = float(input(("第4个")))

max_value = num1
if max_value < num2:
    max_value = num2
if max_value < num3:
    max_value = num3
if max_value < num4:
    max_value = num4
print(max_value)
