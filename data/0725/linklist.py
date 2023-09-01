class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next



class LinkList:
    def __init__(self):
        self.head = Node(None)

    def init_list(self,list_):
        p = self.head
        for item in list_:
            for item in list_:
                p.next = Node(item)
                p = p.next
    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val)
            p = p.next

    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def clear(self):
        self.head.next = None

    #尾部插入
    def append(self,val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    #头部插入
    def head_insert(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
    #指定插入位置
    def insert(self,index,val):
        p = self.head
        for i in range(index):
            #超出位置最大范围结束循环
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node
    #删除节点
    def delete(self,x):
        p = self.head
        #结束循环必然两个条件其一为假
        while p.next and p.next.val != x:
            p = p.next
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next

    #获取某个节点值，传入节点位置获取节点值
    def get_index(self,index):
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("list index out")
            p = p.next
        return p.val