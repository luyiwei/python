list_ticket = []
while len(list_ticket) < 6:
    ticket = int(input("输入:"))
    if ticket < 1 or ticket > 33:
        print("不在范围:")
    elif ticket in list_ticket:
        print("重复:")
    else:
        list_ticket.append(ticket)
# print(list_ticket)

while len(list_ticket) < 7:
    bule_ticket = int(input("输入篮球："))
    if 1 <= bule_ticket <= 16:
        list_ticket.append(bule_ticket)
    else:
        print("重新输入")
print(list_ticket)