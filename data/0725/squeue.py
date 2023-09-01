"""
1.基于列表完成数据存储
2. 通过封装规定数据朝左
"""
#自定有队列异常
class QueueError(Exception):
    pass
class SQueue:
    #初始化
    def __init__(self):
        self._elems = []

    #判断队列是否为空
    def is_empty(self):
        return self._elems == []
    #入队 列表尾部定义为队尾
    def enqueue(self,val):
        self._elems.append(val)

    #出队
    def dequeue(self):
        if not self._elems:
            raise QueueError("Stack is empty")
        return self._elems.pop(0)


if __name__ == "__main__":
    sq = SQueue()
    # sq.enqueue(10)
    # sq.enqueue(20)
    # sq.enqueue(30)
    # while not sq.is_empty():
    #     print(sq.dequeue())
    for i in range(10):
        sq.enqueue(i)
    from sstack import *
    st = SStack()
    while not sq.is_empty():
        st.push(sq.dequeue())
    while not st.is_empty():
        sq.enqueue(st.pop())

    while not sq.is_empty():
        print(sq.dequeue())