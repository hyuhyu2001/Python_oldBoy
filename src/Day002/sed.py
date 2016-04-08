#-*- coding:UTF-8 -*-
'''
tuple 元组（即常量数组），常量即不可变的量，一旦形成，里面的值不可改变，定义了，不让人随便改
tuple = ('a','b','c','d','e')
可以用list的[],:操作符提取元素。
sed是替换


a = ('1','2','3','4')
#用法只有a.count();a.index(),，没有增删改查,是只读的，不可修改

print a.index('1')
print type(a)
#列表和元组是可以互相转换的
print list(a)  #元组改为列表
print tuple(a) #列表改为元组
'''

#开发文件替换小程序

import sys,os

if len(sys.argv) <= 4:
    print "usage:./file_replace.py old_text new_text filename"
old_text,new_text = sys.argv[1],sys.argv[2] #一行可以申明两个变量
file_name = sys.argv[3]


f = file(file.name,'rb')
new_file = file('.%s.bak' %file_name,'wb') #加个点就是隐藏文件打开,new file for writing
for line in f.xreadlines(): #loop old file and replace the old text to new text
    new_file.write(line.replace(old_text,new_text)) #write replaced line into new file
f.close()
new_file.close()

if '--bak'  in sys.argv:
    os.rename(file_name,'.%s.bak2'  %file_name) #unchanged
    os.rename('.%s.bak'  %file_name,file_name) #changed
else:
    os.rename('.%s.bak'  %file_name,file_name) #replace old file