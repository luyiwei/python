"""
数据库操作模块
思路：
将数据库封装一个类，将dict_server需要的数据库操作功能分别写成方法，在dict_server中实例化对象，需要什么
方法直接调用
"""
import pymysql
import hashlib
SALT = "as89213"  #盐
class Database:
    def __init__(self,host='172.16.70.211',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database=None,
                     charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.connect_database() #连接数据库
    #连接数据库的函数
    def connect_database(self):
        self.db = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,database=self.database,charset=self.charset)
    #关闭数据库
    def close(self):
        self.db.close()
    #创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()
    #注册操作
    def register(self,name,passwd):
        sql ="select * from user where name='%s'%name"
        self.cur.execute(sql)
        r = self.cur.fetchone() #查找到返回元组，查不到返回none
        #查找到用户存在
        if r:
            return  False


        hash = hashlib.md5((name+SALT).encode()) #加盐
        hash.update(passwd.encode()) #算法加密
        passwd = hash.hexdigest()  #加密后的密码
        #插入数据库
        sql = "insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False
    #登录处理
    def login(self,name,passwd):
        hash = hashlib.md5((name + SALT).encode())
        hash.update(passwd.encode)
        passwd = hash.hexdigest()
    #数据库查找
        sql = "select * from user where name='%s' and passwd='%s'"%(name,passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        #有数据则允许登录
        if r:
            return True
        else:
            return False
    #查单词
    def query(self,word):
        sql = "select mean from words where word='%s'"%word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        #如果找到r---》（mean）返回元组否则为none
        if r:
            return r[0]
    #插入历史记录
    def insert_hist(self,name,word):
        sql = "insert into hist (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception:
            self.db.rollback()
    #历史记录查询
    def history(self,name):
        sql = "select name,word,time from hist where name='%s' by time desc limit 10"%name
        self.cur.execute(sql)
        return self.cur.fetchall()