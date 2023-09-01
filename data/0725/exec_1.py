"""

"""
from lstack import *

#将验证条件提前定义好
parens = "()[]{}" #特殊处理字符集
left_parens = "([(" #入栈字符集
# 验证匹配关系，键值对
opposite = { '}':'{',']':'[',')':'('}

ls = LStack() #存储括号的栈

#编写生成器，用来变量字符串，不断的提供括号及其位置
def parent(text):
    # i 遍历字符串的索引位置
    i,text_len = 0,len(text)
    #开始遍历字符串
    while True:
        while i < text_len and  text[i] not in parens:
            i += 1
        # 到字符串结尾
        if i >= text_len:
            return
        else:
            yield text[i],i
            i +=1
# 功能函数判断提供的括号是否匹配
def ver():
    for pr,i in parent(text):
        if pr in left_parens:
            ls.push((pr,i)) #左括号入栈
        elif ls.is_empty() or ls.pop()[0] !=opposite[pr]:
            print("Unmatching is found at %d for %s"%(i,pr))
            break
    else:
        if ls.is_empty():
            print("yes")
        else:
            d = ls.pop()
            print("Unmatching is found at %d for %s"%(d[1],d[0]))
