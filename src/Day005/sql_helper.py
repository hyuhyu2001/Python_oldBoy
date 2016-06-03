#!/user/bin/env python
#encoding:utf-8

'''
类里面有增删改查
三层架构之公共层、配置文件
'''

import MySQLdb
import conf

class MySqlHelper(object):
    
    def __init__(self):
        self.__conn_dict = conf.conn_dict  #调用conf文件，取数据库的连接串
    
    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1234',db='07day05db')
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        
        reCount = cur.execute(sql,params)
        data = cur.fetchall()  #获取表里所有数据
        
        cur.close()
        conn.close()
        return data
    
    def Get_one(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)  #调用配置文件，注意加两个星号（加一个星是列表，加两个星是字典）
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        
        reCount = cur.execute(sql,params)
        data = cur.fetchone()  #获取表里所有数据
        
        cur.close()
        conn.close()
        return data
    
helper = MySqlHelper()
sql = "select * from admin where id>%s"
params = (1,)
simple = helper.Get_one(sql,params)
dict_data =  helper.Get_Dict(sql,params)