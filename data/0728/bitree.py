"""
bitree.py 二叉树得简单实践
1.使用链式存储，一个Node表示一个树得节点
2.节点考虑使用两个属性变量分别表示左连接和右连接
"""
# 二叉树节点
class Node:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right

#二叉树遍历类
class Bitree:
    def __init__(self,root = Node):
        self.root = root
    #先序遍历
    def preOrder(self,node):
        if  node is None:   #终止条件
            return
        print(node.val)
        self.preOrder(node.left) #函数套函数，如果执行结果为None 这执行上一层函数
        self.preOrder(node.right)
    #中序遍历
    def inOrder(self,node):
        if node is None:
            return
        self.preOrder(node.left)
        print(node.val,end = "")
        self.preOrder(node.right)





if __name__ == "__main__":
# B F G D I H E C A
#根据后续遍历构建二叉树
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D',f,g)
    i = Node('i')
    h = Node('h')
    e = Node('E',i,h)
    c = Node('c',d,e)
    a = Node('A',b,c)  #根
#将a作为遍历得起始位置
    bt = Bitree(a)
    bt.preOrder(bt.root)