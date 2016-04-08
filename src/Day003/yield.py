#!/user/bin/env python
#encoding:utf-8

'''
#xrange延迟技术：只有在遍历的时候才会创建一个（每次循环创建一个整数，延迟创建），没有遍历的时候只是一个生成器
print range(10)
print xrange(10)  
for item in xrange(10): 
    print item

from aifc import data
from plistlib import Data
from distutils.tests.setuptools_build_ext import if_dl

函数里定义yield，调用函数时返回的是一个生成器，而不是生成的值
而生成器只有在遍历的时候，函数里的代码才执行，并且每次循环时只执行一条

#遍历第一条时执行yield1，遍历第二条时执行yield1和yield2，目的是暂时保存执行的位置
def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
re = foo()
for item in re:
    print item


#yield高级示例
def AlexReadlines():
    seek=0  #默认从文件的开始处读
    while  True:
        with  open ('d:temp.txt','r') as f: #通过with可以不用主动close
            f.seek(seek) #根据字节跳到某一个字节处
            data = f.readline()
            if data:
                seek = f.tell() #tell获取行末的字符位置
                yield Data
            else:
                return  #return之后，整个函数退出

for item in AlexReadlines():
    print item

#yield，多线程池，做为一个池子，什么时候用什么时候拿过来，延迟生成
#还一个作用，可以保存函数的执行状态
#一个函数开始调用，执行完毕才开始返回，中间的状态就无法对外面告知，不能被外界获取，在函数执行过程中，不用等待函数执行结束（执行一半，也不阻塞）
#一个函数调用，执行要10分钟，调用时立马给返回值，但此时函数没退出，挂起，程序运行继续调用一次，再继续调用，如此便不会阻塞，可以支持多线程

#三元运算以及lambda表达式
temp = None
if 1>3:
    tmp = 'gt'
else:
    temp = 'lt'
print temp
#三元运算,如此简洁的运算，一次性搞定，便是三元运算
result = 'gt' if 1>3 else 'lt'
print result
'''
#lambda表达式，相当于执行了一个函数 ，一个temp变量，接受了两个参数x和y，也可以定义一个参数或者多个 temp = lambda x:x*y 
temp = lambda x,y:x+y  #lambda为匿名函数（就是没有名的函数）
print temp(4,10)
'''
def foo(x,y)
    return x+y

print foo(4,10)
'''

print map(lambda x:x*2,range(10))
print map(lambda x:x**x,range(10))

