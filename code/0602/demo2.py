# a = 0.01 / 1000
# count = 0
# while a < 8844.43:
#     a *= 2
#     count += 1
# print(count)

import random
random_number = random.randint(1,100)
print(random_number)
count = 0
while True:
    num = int(input("输入"))
    count += 1
    if random_number > num:
        print("小")
    elif random_number < num:
        print("大")
    else:
        print("对,"+str(count)+"次")
        break

