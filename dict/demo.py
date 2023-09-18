"""
功能模块
网络搭建
注册
登录
查单词
历史记录
设定客户端服务器端协议
注册 R
登录 L
查单词 Q
历史记录 H
退出 E
"""
while True:
    print("一级级界面")
    cmd = input()
    if cmd == 'in':
        while   True:
            print("二级")
            cmd = input()
            if cmd == 'out':
                break
