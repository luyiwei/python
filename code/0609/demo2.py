dict01 = {}
while True:
        name = input("名称:")
        if name == "":
            break
        price = int(input("单价:"))
        dict01[name] = price
for k,v in dict01.items():
    print("%s商品单价是%d"%(k,v))


