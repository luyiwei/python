list01 = ["aa","bb","ccc"]
dict01 = {}
for i in list01:
    dict01[i] = len(i)
print(dict01)
dict01 = {i:len(i) for i in list01}
print(dict01)

list02 = [101,102,103]
dict02 = {}
for item in range(len(list01)):
        dict02[list01[item]] = list02[item]
print(dict02)
dict02 = {list01[item]:list02[item] for item in range(len(list01))}
print(dict02)
