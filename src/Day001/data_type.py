#-*- coding: UTF-8 -*-  可以将中文存储，否则会按ASSIC码存储

print(3<>3)

a=2**12
print type(a)

a=2**32
print type(a)

print type(3.14)

name='alex'
print type(name)
if type(name) is str:print name

name_list = ['alex','rachel','erion']
print type(name_list)

name = {'alex':[28,'IT']}
print name['alex']
print type(name)

a='alex'
print type(a)

a=u'alex'  #存储占两个字节
print type(a)

a=u'alex'
print type(a)

name=u'李雪'
print len(name)
print type(name)
print name.encode('utf-8')  #转换为utf-8
print name.decode('utf-8')  #转换为Unicode


'''
一、按特性划分
1、数字类型
整形
（1）布尔型，只有两个值，True和False(首字母大写)
（2）长整形 long：当比较长的时候，会自动转换为长整形,直接用标准整形就可以
（3）标准整形 int
非整形float
（1）双精度浮点型
（2）复数
（3）decimal（不是内建类型）
2、序列类型：数组
（1）字符串str
（2）元组tuple
（3）列表list
3、映射类型
字典dict:有 key和value,解决普通变量不能存储太多的信息
4、集合类型
（1）可变集合set
（2）不可变集合frozenset
二、按可变性划分
1、可哈希的，不可变数据类型
（1）数字类型
（2）不可变集合
（3）字符串
（4）元组
2、可变数据类型
（1）字典
（2）列表
（3）可变集合
'''