class Vector1:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return "结果"+str(self.x)
    def __add__(self, other):
        # print("参数",other)
        return Vector1(self.x + other)
v01 = Vector1(10)

print(v01 + 2)
v01 += 4
print(v01)