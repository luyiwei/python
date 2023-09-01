# a = ord("a")
# print(a)
# str01 = chr(97)
# print(str01)

# str_input = input("输入:")
# for i in str_input:
#     print(ord(i))

while True:
    str_input = input("输入:")
    if str_input == "":
        break
    else:
        print(chr(int(str_input)))