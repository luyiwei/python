"""
标准读操作 select
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
#获取数据库数据
sql = "select * from aa where id=1;"
cur.execute(sql) #执行正确后cur调用函数获取结果
#获取一个查询结果
one_row = cur.fetchone()
print(one_row) #元组
#获取多个查询结果
many_row = cur.fetchmany(2) #参数写几个，就获取几个结果
#获取所有查询结果
all_row = cur.fetchall()
#关闭数据库
cur.close()
db.close()