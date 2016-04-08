#!/user/bin/env python
#encoding:utf-8
import re

'''
re模块：正则表达式：正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

result1 = re.match('\d+', 'dsdsad123ada') #正则表达式；字符串;通过正则表达式，去字符串里匹配【\d找的是数字】
if result1:
    print result1.group() #数字123放在后面，则匹配不到，因为match从开始匹配
else:
    print 'nothing'
result2 = re.search('\d+', 'dsdsad123ada')  #match只能从字符串的起始位置进行匹配，search是从整个字符串、整个内容里匹配
print result2   
print result2.group()

#findall,会将字符串所有匹配的找出来，match和search只找一个
result3 = re.findall('\d+', 'dsd111sad222a333d444a')
print  result3 

#compile,通过compile编译生成对象，后面在通过其他方式找
#假如在100多个字符串，得编译100次，寻找100次，通过compile只编译一次，后面直接寻找即可 
#compile = re；；re的逻辑即是先compile，然后match
#只能一次寻找一个字符串，不能一次寻找多个字符串
com = re.compile('\d+')  
print com.findall('dsd111sad222a333d444a')
print type(com)
'''

#分组的方式
result2 = re.search('(\d+)\w*(\d+)', 'dsdsad123abcd234da')    
print result2.group()  #group会将所有符合的表达式拿出来
print result2.groups() #groups只获取组里的东西
#group与groups区别，gruop只跟正则表达式里的分组有关系
#字符： \d是数字；\w就是代表下划线、字母、数字，中横岗; \t是制表符 ; . 是除了回车以外的所有字符
#次数： *代表>=0;+代表>=1;?代表0或1；{m}是次数；{m,n}是范围，比如{3,5}包含3和5；即是匹配哪个字符，以及这个字符出现的次数
#30分钟正则表达式（网上百度）

result4 = re.search('a{3,5}', 'aaaaa')   
print result4.group()

#日志处理经常用正则表达式；
#匹配IP地址

ip = '12.34.43.dsadafff.fef!~ddfaf192.168.32.43_w342d@#9436'
print re.findall('\d+\.',ip)
#简单的办法
print re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)
#装逼的做法
print re.findall('(?:\d{1,3}\.){3}\d{1,3}',ip)