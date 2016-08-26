#!/user/bin/env python
#encoding:utf-8

'''
三层架构之model层和UI层
'''
from sql_helper import MySqlHelper #把utility模块下sql_helper文件中的MySqlHelper类导入进来

class Admin(object):
    
    def __init__ (self):
        self.__helper = MySqlHelper()
        
    def Get_one(self,id):
        sql = "select * from admin where id =%s"
        params = (id,)
        return self.__helper.Get_one(sql,params)
    
    def CheckValidate(self,username,password):
        sql = 'select * from admin where name =%s and password=%s'
        params = (username,password,)
        return self.__helper.Get_one(sql,params) #sql语句传到Get_one，并且把结果返给我，返给我后，再返回给调用方
            