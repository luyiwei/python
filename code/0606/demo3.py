list_person = []
while True:
    str_input = input("输入:")
    if str_input == "":
        break
    list_person.append(str_input)
for i in list_person:
    print(i)