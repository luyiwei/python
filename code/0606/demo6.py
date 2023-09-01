# list01 = [800,1000]
# list02 = list01[:]
# print(list01[:])
list01 = [54,25,12,42,35,17]
list02 = []
for i in list01:
    if i > 30:
        list02.append(i)
print(list02)

max_value = 0
for item in range(5):
    number = int(input("第%d数字:"%(item+1)))
    if max_value < number:
        max_value = number
print(max_value)

