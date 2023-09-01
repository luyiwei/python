"""
abcdefce
"""
dict01 = {}
str_target = "abecdefce"
for i in str_target:
    if i in dict01:
        dict01[i] += 1
    else:
        dict01[i] = 1
print(dict01)