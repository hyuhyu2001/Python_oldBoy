#!/user/bin/env python
#encoding:utf-8
'''
python语言写的内置函数，通过一个函数就执行一个很复杂的操作
help()
dir()
vars()
type()
import temp  导入某个模块，第一次导入会执行模块里的所有代码，第二次导入时就不做重复的工作
reload(temp)
id() 查看变量的内存地址


#help('lambda')  #帮助

#dir列出所有的key，vars列出所有的key和value
a = []
print dir()  #把列表的所有内置函数都通过字符串的形式列出来
print vars()  #一个*号，代表字典  print vars(*a)

print type(a)#看传递的参数是什么类型

from file import demo #第一次导入模块，执行代码成功
reload (demo)  #第二次导入，通过reload进行重新导入


print abs(-9)  #绝对值
print bool(0)  #布尔类型 0位假，1位真，15、-1为真
print divmod(9, 3)   #被除数除以除数等于商  余数  做分页的时候用（余数>0时页数+1）
print max([11,22,33,333]) #最大值 ，只能传一个列表
print min([11,22,33,333]) #最小值
print sum([11,22,33,333]) #求和
print pow(2,10)  #质数  2**10 相当于x的y次方


print len('中文')  #列表的长度，汉子的长度，如果是中文，则是字节的长度
#all判断列表的所有内容，如果全为真才是True，有一个为否，则为False
print all([1,2,3,0]) #可迭代的东西，有一个为假 False
print all([1,2,3,1]) #可迭代的东西，所有都是真才是  True
#any判断列表的所有内容，如果全为否才是False，有一个为真，则为True
print any([0,0,0,0]) #可迭代的东西，全为否  False
print any([1,2,3,0]) #可迭代的东西，有一个为真便是  True

print bool() #空值为False
print bool(None)  #None为False

#可以支持，动态生成验证码
print chr(65)  #ascII对应得字符
print ord('A')  #验证码生成，随机
print hex(20)  #转换为16进制
print oct(20) #转换为8进制
print bin(20)  #转换为2进制


li = ['手表','汽车','房']
for item in li:
    print item

#场景：商品列表加序号,默认加了序列，默认从0开始;;加一个参数1，默认从1开始
for item in enumerate(li,1):
    print item[0],item[1]  #找索引名
       
for k,v in enumerate([1,2,3,4]):
    print k,v
    
#%s的另一种应用，，format为字符串的格式化
#%s是占位符，{0}是第一个占位符，{1}是第二个占位符
s = 'i am {0},{1}'
print s.format('alex','xxx')
str(1)

def Function(arg):
    print arg

print apply(Function,('123'))  #执行函数，类型Function('alex'),应用不广泛

#普通版，为列表每一个数字加100
li = [11,22,33]
temp = []
for item in li:
    temp.append(item+100)
print temp

#map函数版
def foo(arg):
    return arg + 100
for item in li:
    temp.append(foo(item))
print temp

#过渡版
temp = map(foo,li)
print temp
#终极版
print map(lambda arg:arg+1,li) 

print map(lambda x:x+1,[1,2,3]) #all,遍历后面序列的每一个元素，执行操作并返回，执行几个元素，返回几个元素

def foo(arg):
    if arg<22:
        return True
    else:
        return False
li = [11,22,33]
print filter(foo, li) #foo为过滤条件，filter只显示为true的序列

print filter(lambda x:x==1,[1,23,4]) #True序列，对序列的每一个元素进行操作，用作过滤

li = [11,22,33]
print reduce(lambda x,y:x+y,li) 
print reduce(lambda x,y:x+y,[1,2,3]) #累计：累加，累乘，对序列的每一个元素进行操作，参数是变动的
#reduce与map和filter的区别是，reduce只接受两个参数，不接受1个和3个参数

x = [1,2,3,5]
y = [4,5]
z = [4,5,6]
q = [8,6,1]
print zip(x,y,z,q)  #传N个列表，生成新的序列，让每一列是一个组;如果列不足，则显示最短的列

print 8*8
a = '8*8' #这是个字符串，字符串的运算，正常split，然后转换为数字
print eval(a) #导数据时，从excel导出后为string类型

com = compile('1+1','','eval')
print eval(com)
'''

#提升B格，反射：以字符串的形式导入模块，并以字符串的形式执行函数
#用于大型数据库，随时要切换数据库，降低程序的耦合
#两个函数__import__ ;getattr()
#hasattr()判断模块，有没有这个函数：判断一个对象是否有某个属性
#delattr()删除这个模块的函数
#getattr() 用户返回一个对象属性，或者方法

temp= 'sys'
model = __import__(temp) #加入3个模块，一个操作mysql，一个操作sqlserver：比如一个mysql宕机了，可以去sqlserver申请
#通过字符串的形式导入模块，比如import sys
#__import__可以动态的导入数据，可以在数据变化时，一键进行切换
print model.path


temp= 'file'  #模块的名字
func = 'count' #函数的名字

model = __import__(temp) 
ob =  getattr(model,'count')  #去model模块，找count函数,并以字符串的形式返回
print ob()

