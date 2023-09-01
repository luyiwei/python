sum = 0
for i in range(10,51):
    if i % 10 == 2 or i % 10 == 5 or i % 10 == 9:
        continue
    sum += i
print(str(sum))