# "How are you" --> "you are How"
str01 = "How are you"
list_result = str01.split(" ")
print(list_result)
list_result02 = list_result[::-1]
print(list_result02)
str02 = " ".join(list_result02)
print(str02)