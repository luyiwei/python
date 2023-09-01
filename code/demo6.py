int_a=int(input("输入数字："))
# unit01 = int_a % 10
# unit02 = int_a // 10 % 10
# unit03 = int_a // 100 % 10
# unit04 = int_a // 1000
# sum = unit01 + unit02 + unit03 + unit04
# print("结果：" +str(sum))
#方法2
result = int_a % 10
result += int_a // 10 % 10
result += int_a // 100 % 10
result += int_a // 1000
print("结果：" +str(result))