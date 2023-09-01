"""
mysql操作基本流程
"""
import pymysql
#连接数据库
db = pymysql.connect(host='172.16.70.211',
                     port=3306,
                     user='root',
                     password='123456',
                     database='test',
                     charset='utf8')
#获取游标(操作数据库，执行sql)
cur = db.cursor()
#执行sql
sql = "insert into aa values (2);"
cur.execute(sql) #执行语句
db.commit() #将写操作提交，多次写操作可以一同提交
#关闭数据库
cur.close()
db.close()
