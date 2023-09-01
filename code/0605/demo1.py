import random
score = 0
for i in range(3):
    a = random.randint(1,10)
    b = random.randint(1,10)
    if int(input(str(a)+ "+" +str(b)+"答案")) == a + b:
        score += 10
print("得分"+str(score))