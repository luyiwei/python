import random
# list01 = []
# list02 = []
# for i in range(1,34):
#     list01.append(i)
# print(list01)
# while True:
#        str_ran = random.randint(1,33)
#        if str_ran not in list02:
#            list02.append(str_ran)
#        if len(list02) > 5:
#            break
# print(list02)

list_ticket = []
while len(list_ticket) < 6:
    random_number = random.randrange(1,33)
    if random_number not in list_ticket:
        list_ticket.append(random_number)
print(list_ticket)
list_ticket.append(random.randrange(1,16))
print(list_ticket)
