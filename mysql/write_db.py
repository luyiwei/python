"""
标准写操作 insert update delete
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
#写数据库
try:
    #sql语句执行
    #插入操作
    id = input('id:')
    print(id)
    sql = "insert into aa (id) values ('%s');"%(id)
    print(sql)
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback() #退回到commit执行之前的数据库状态
    print(e)
#关闭数据库
cur.close()
db.close()