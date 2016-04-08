#-*- coding:UTF-8 -*-
'''
字典，假如列表中有一百万个元素，想找某个值，一个个循环找出来
所以为了快速定位到我想要查的值，字典便应运而生
字典先对一组数据生成一个索引列表，直接去索引（key）直接去查找相应的值  key value，先找key，key对应相应的value
字典非常重要的一点：所有的key必须是唯一的，不能有重复的key，且字典的key不可变
字典里可以包含列表，列表里可以包含字典
字典里可以存储列表、变量、字典等等
'''
#---key,value--
name_info = {
    'name':'jacky',
    'age':'29',
    'job':'Engineer'
}


name_info['salary'] = 3000  #相当于新增
name_info['job'] = 'test' #原先字典已存在job，故此是更新操作
'''
print name_info['name'] #通过key，打印出对应的value
#name_info.pop('salary') #删除salaey
#name_info.popitem()  #如果不指定，则随机删除一个,因为字典默认是没有排序的 ，因为字段可以通过key找到value，所以默认不排序 

print name_info

#同时打印key和value
for i in name_info:  #效率高
    print i, name_info[i] #随机打顺序
    
for k,v in name_info.items(): #效率低，因为要先转换为列表
    print k,v
    
print name_info.items() #打印key和value

print name_info['user']  #user 在字典不存在，则报错
print name_info.get('user')   #用get的方式，虽然user不存在，但不报错，会报null的错误
print name_info.has_key('user')  #经常用到的，先判断key是否存在，如果不存在，则后续创建
print name_info.iteritems()
print name_info.keys()  #只显示key
print name_info.values() #只显示value
print name_info.setdefault('stuid',1123) #只显示value 如果字典里没有1123，则增加1123，如果里面有，则不覆盖
print name_info.setdefault('stuid',2234)  #因为已经有，所以不覆盖。生成默认值时用的比较多
a = {
     'age':39,
     'job':'develop',
     'add':'beijing'
 }
print name_info.update(a) #update(a),将a字典里的值赋值给nama_info；如果存在，则update，如果不存在则insert
'''
info2 = name_info  #别名
name_info['job'] = 'HR'  #任意一个变，另外一个字典都会变
info2['salary'] = '5000'   
#print name_info.copy()  #给他进行一个肤浅的复制，浅复制
#info2和name_info中job的内存还是一样：为了减少内存，所以这么做（字典原先是100万，所以不克隆，只是软链接）
#如果想拷贝，新生成新的内存，则用copy
print id(info2['job'])  
print id(name_info['job'])
print name_info
print info2
info3 = name_info.copy()  #浅拷贝
print id(info3['job'])  
name_info['sex'] = 'M'
print info3
#字典里添加列表
name_info['ex_list'] = ['corel','erion','lady']
info4 = name_info.copy()
name_info['add'] = 'HongKong'  #第一层的可以改变
name_info['ex_list'].append('wutenglan')  #肤浅的赋值，列表里更新，info4和name_info都改变了
print info4
print name_info

#深copy,第二层的也会分别独立，但非常耗空间
import deepcopy
import copy
info5 = copy.deepcopy(name_info)