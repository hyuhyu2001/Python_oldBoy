#-*- coding:UTF-8 -*-
'''
集合非常重要
SET集合
特点：无序；元素不重复
功能：关系测试，去重
字典对应的value可以重复，但是集合默认就是不重复，里面每一个元素都是唯一的
把列表变成集合后，自动会去重
'''
'''
name_set = {1,2,3,4} 
name_set = set([1,2,3,4])
name_set = {1,2,3,4,2}  #增加的时候自动去重

print name_set

a = range(100)
a = set(a)

#print a[1]  #没有下标，没有排序，所以取不出来，所以是无序的
for i in a:print i  #循环，打印出每一个

a.add(-1)
a.add(1)
a.add(100)

print a
'''

x = {1,2,3,4}
y = {3,4,5,6}
#非常有用
#测试x和y之间的关系，有交集、并集、合集，x里的数据，在y里是不是也有
#交集,即在A，又在B
print x & y
#并集  或 ，在x中，或者在Y中
print x | y
#求x和y里的差集  在x里有，但是在y里没有
print x - y
#求y和x里的差集  在y里有，但是在x里没有
print y - x
#对称差集 是交集的反集，把两个都有的去掉，把都没有的显示出来
print x ^ y
z = {1,2,4}
print z.issubset(x)  #z是x的子集，所以打印是True
print x.issuperset(z)  #x是z的父集，所以打印是True
