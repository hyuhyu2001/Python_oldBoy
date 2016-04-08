#-*- coding: UTF-8 -*-
#变量variable与常量constant
PAI = 3.1415926
x=2
y=3
z=x+2
print id(x)
x=5
print x+y
print 'z:',z
print id(z)
print 'x:',x
print id(x)

#运算 优先级（先乘除，再加减）
print 1+1*3/2
print 3/2 #只能等于1，如果想运算准确，需要把3改为浮点数3.0
print 1+1*3.0/2
print (1+1)*3.0/2
print (1+1)*3/2
print 2**32 #求多少次方
print 9.0/2.0
print 9.0//2.0

#双引号里面嵌套单引号
print "hello,my name's alex li"

'''1、变量就是可变的，常量就是不变的量；
2、写代码时大写的一般就代表常量，小写的就代表变量
3、第一次是定义X,第二次的X重新修改值"
4、为什么打印时z=2，而不是等于5？每次更改前会有一个内存机制，所以后面更改时会针对原先的内存
    通过id指向内存地址,看是否指向相同的内存地址，是完全独立的数据
变量命名规则
1、标识符的第一个字符必须是字母表中的字母（大写或者小写）或者一个下划线（“_”）
2、标识符名称的其他部分可以由字母（大写或者小写）、下划线（“_”）或者数字（0-9）组成
3、标识符是对大小写敏感的，例如myname和myName不是同一个标识符
4、有效标识符名称的例子：_my_name、name_23和alb2_c3
    无效标识符的例子有2things（数字开头）、this is spaced out（空格） 和 my-name（横杠代表是减号）
5、起变量的风格：定义变量为了以后来调用，变量存储什么东西能明确出来，尽量用名词，尽量分开，比如task_detail,TaskDetail,taskDetail
二进制十进制十六进制的转换 计算机中0表示False假 ，1表示为True
6、单行注释 一个# ；多行注释 前后个 三个单引号，只要前后有3个单引号就行，中间的不用关心 
7、单引号与双引号的区别：没区别，但是单引号外面嵌套时，需要用双引号
'''