#!/user/bin/env python
#encoding:utf-8


'''
三层架构之公共层
'''
#自增长，系统自己增长

import MySQLdb

#打开门
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1234',db='07day05db')
#伸手
cur = conn.cursor()

#数据操作层
#select数据
reCount = cur.execute('select * from admin')
data = cur.fetchall()  #获取表里所有数据

#把手缩回来
cur.close()
#关闭门
conn.close()

print reCount  #影响了多少行数，比如数据库有两条记录，显示为两条
print data  #打印所有数据


#数据操作层
#insert数据
sql = 'insert into admin (name,address) values(%s,%s)' #%s相当于占位符,只认%s，和输入符不一样
params = ('alex_1','usa')
reCount = cur.execute(sql,params)
conn.commit() #insert/update/delete时必须加入commmit,commit是所有语句全部提交一次

print reCount

#delete数据
sql = 'delete from admin where id=%s' 
params = ('n1',)
reCount = cur.execute(sql,params)
conn.commit() #insert/update/delete时必须加入commmit

#update数据
sql = 'update admin set name=%s where id=7' 
params = ('stbs',)
reCount = cur.execute(sql,params)
conn.commit() #insert/update/delete时必须加入commmit


#把excel表里的数据全部录入到数据库中，不建议在打开数据库之外用for循环，因为会每次打开数据库，而且会影响数据库连接池
#要打开一次连接，插入多条数据，把excel放入列表中，一次性同时插入多个数据
#用executemany

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1234',db='08day05')
cur = conn.cursor()

li =[
     ('alex','usa'),
     ('sb','usa'),
]

reCount = cur.executemany('insert into UserInfo(Name,Address) values(%s,%s)',li)

conn.commit()
cur.close()
conn.close()

print reCount

#事务操作（多个操作时）
conn.commit()  #提交，两条语句都执行提交成功后，才会commit，否则不会提交（范围是commit前的语句）
conn.rollback()  #回滚，两条语句，第一条语句正确，第二条语句错误时，便会回滚，使第一条语句不执行

#执行结果后想知道表里字段的名字，改为字典的形式，通过下述方式实现，获取数据的时候根据字典类型的拿过来
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

#fetchall：获取所有数据
#fetchone：只获取一个，只获取第一条数据，再用一次fechone是拿第二条数据，比如连续用两次fetchone
data = cur.fetchone()
print data
data = cur.fetchone()
print data

#指针的两个模式
cur.scroll(-1,mode='relative')  #绝对定位，来回走的过程
print cur.fetchone()
print cur.fetchone()
cur.scroll(0,mode='absolute') #相对定位，来回走的过程
print cur.fetchone()
print cur.fetchone()

#fetchmany 获取多个
#插入一条数据时候怎么获取自增iD?通过返回值实现
print cur.lastrowid #上传之后，获取当前数据的ID，，比如实现两个表的外键，lastrowid当做另一个表的参数


