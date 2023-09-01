list01 = [i ** 2 for i in range(1, 11)]
print(list01)
list02 = [i for i in list01 if i % 2 !=0]
print(list02)
list03 = [ i for i in list01 if i % 2 == 0]
print(list03)
list04 = [ i+1 for i in list01 if i % 2 == 0 and i > 5 ]
print(list04)
