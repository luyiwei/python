list01 = ["a","b","c"]
list02 = ["A","B","C"]
list03 = []
for i in range(len(list01)):
    for j in range(len(list02)):
        list03.append(list01[i] + list02[j])
print(list03)
list03 = [ list01[i] + list02[j] for i in range(len(list01))    for j in range(len(list02))]
print(list03)