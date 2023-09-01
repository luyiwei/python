"""
二分查找
"""
def search(list_,key):
    #第一个数得index，最后一个数得index
    low,high = 0,len(list_) -1
    #循环每次去除一半内容
    while low <= high:
        mid = (low + high) // 2
        # 取后半部分
        if list_[mid] < key:
            low = mid + 1
        #取前半部分
        elif list_[mid] > key:
            high = mid - 1
        else:
            return mid
l = [4,9,3,1,2,5,8,4]