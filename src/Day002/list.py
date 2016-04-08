#-*- coding:UTF-8 -*-

#数组，在python中称为列表，一个变量只用字符串的形式，存的信息非常有限，列表属于数组的一种

name_list = ['alex','jack','old boy','jack']
'''
print name_list[1]  #通过位置取值
'''
name_list.append('Eric')  #最后插入一行

name_list.insert(2,2) #在第二行插入

#name_list.remove('old boy') 删除某一行，删除第一次出现的该元素，
#del name_list[2]#按下标删除 

#print name_list

#print name_list.count('jack') #统计jack出现多少次

#print name_list.index('jack')   #找到jack所在列表的位置，只返回第一个，如果无则抛异常

#内存里保存着索引的位置，列表有序是非常重要的一个概念，列表索引保证其有序
#name_list.reverse() #把排序反转，倒序
#name_list.sort()  #对列表进行排序，按ASCII里的顺序排列
infos = [1 ,2 ,3 ,4 ,5 ,6 ]
#name_list.extend('abcd')#把一个字符分开，分别导入到列表中，主要作用把第二个列表加入到第一个列表中,
name_list.extend(infos) #用法与name_list +=infos相同
print name_list
print name_list[2:5] #给列表切片,比如切234顾头不顾尾（把2取出来，但是不取5，所以一般要加1）
print name_list[-5:] #取最后的5个
print name_list[-5:-1] #取最后的5个，负数是从右往左，由-0开始，所以这里是-1
print name_list[:5]#取前5个
name_list[name_list.index(2):name_list.index(2)+4] #通过index找出位置，再运算找到后面的位置
print name_list[1::2] #隔一个取一个，可快速实现奇偶数的取法
print name_list[1::3] #隔两个取一个
print name_list[::2] #只取偶数
print name_list[1::2] #只取奇数

#把所有2的位置找出来，默认是找第一个2的位置【先找第一个位置，通过第一个位置再找第二个位置】
first_pos = 0 
for i in range(name_list.count(2)):  #循环，按2个位置总数，看循环几次
    new_list =  name_list[first_pos:]  #第一次先从0开始取，取0到最后的位置
    next_pos = new_list.index(2)+1  #下一次循环的位置，2的新位置加1，重新循环  
    
    print new_list
    print 'Find postion:',first_pos + new_list.index(2)  
    first_pos += next_pos #把下一个循环的开始位置改成第二次2后面的位置

