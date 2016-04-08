#!/user/bin/env python
#encoding:utf-8

import time


#1、时间戳：1970年1月1号之后的秒，可读的格式改成unix时间戳
print time.time() #以时间戳的方式存在

#2、元组：包含了年、日、星期等time.struct_time
#print time.struct_time('2015')

#3、格式化的字符串 2014-11-11 11:11 print time.strfttime()
print time.gmtime() #格式化存在
print time.strftime('%Y%m%d %H%M%S') #重要！字符串格式化后的时间 ，怎么展示需要自己定义
print time.strftime('%Y-%m-%d %H:%M:%S') 

#三种格式的相互转换
print time.strptime('2014-11-11', '%Y-%m-%d') #字符串转换为结构化的时间

print time.localtime()  #结构化的时间
print time.mktime(time.localtime()) #结构化的时间改为时间戳
#字符串转时间戳是不支持的