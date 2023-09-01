"""
排序
"""
#选择排序
def select(list_):
    #每轮选出一个最小值，需要len(list_) - 1 轮
    for i in range(len(list_) - 1):
        min = i #假设list_[i]为最小值
        for j in range(i+1,len(list_)):
            if list_[min] > list_[j]:
                min = j
        #进行交换，将最小值换到应该在得位置
        if min != i:
            list_[i],list_[min] = list_[min],list_[i]

#插入排序
def insert(list_):
    #控制每次比较得数是谁，从第二个数开始
    for i in range(1,len(list_)):
        x = list_[i] # 空出list_[i]得位置
        j = i - 1
        while j >= 0 and list_[j] > x:
            list_[j+1] = list_[j]
            j -= 1
        list_[j+1] = x




l = [4,9,3,1,2,5,8,4]
select(l)
print(l)