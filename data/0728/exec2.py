word = input("Word:")
f = open('dict.txt')
for line in f:
    w = line.split(' ')[0]
    #如果遍历到的单词已经大于word就结束查找
    if w > word:
        print("无")
        break
    elif w == word:
        print(line)
        break
else:
    print("no")

f.close()