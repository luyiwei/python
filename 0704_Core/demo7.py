tuple01 = ("aa","bb","cc")
iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

dict01 = {"aa":101,"bb":102,"cc":103}
itera = dict01.__iter__()
while True:
    try:
        key = itera.__next__()
        print(key,dict01[key])
    except StopIteration:
        break