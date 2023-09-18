import getpass #隐藏输入 如：输入密码
import hashlib  #转换加密

#输入隐藏
pwd = getpass.getpass("PW:")  #pycharm不行要在终端上运行

#hash对象
hash = hashlib.md5() #生成对象
#hash = hashlib.md5("#$oasd".encode())  加盐
hash.update(pwd.encode()) #算法加密
pwd = hash.hexdigest()  #提取加密后的密码(返回加密后的字符串)
print(pwd)