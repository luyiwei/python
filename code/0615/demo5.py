# def find_str(*args):
#     """
#
#     :return:
#     """
#     count = 0
#     for i in args:
#         if i == " ":
#             count += 1
str01 = "  校 训:自   强不息 、 厚德载物。   "
print(str01.count(" "))
str02 = str01.lstrip().rsplit()
print(str02)

str03 = str01.replace(" ","")
print(str03)
print(str01.index("载物"))
print(str01.startswith("校训"))