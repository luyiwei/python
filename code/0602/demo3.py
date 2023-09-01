import random
random_number = random.randint(1,100)
print(random_number)
count = 0
while count < 3:
    num = int(input("输入"))
    count += 1
    if random_number > num:
        print("小")
    elif random_number < num:
        print("大")
    else:
        print("对,"+str(count)+"次")
        break
else:
    print("aaa")