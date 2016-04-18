#!/user/bin/env python
#encoding:utf-8

'''
面向对象编程 OOP = object-oriented programming

分类：创建两个类，比如人和兽
然后想造人的话，怎么造？，人在程序里就是真实的对象；创建两个人，a和b，a和b是有不同的
人和类的区别：人是子元素，人与人事不同的
实例化一个人就能创造A，实例化一个人就能创造B

分类（抽象）---创建对象（实例化）
'''
'''
class Alex: #创建alex类
    xx = '没心没肺'

class Person: # 创建人这个类  ：class类的定义，person类的名称
    xue = '血'   #人的公共属性
    rou = '肉'
    def __init__(self,name,age):  #类里必须有__init__，init是初始化，self参数是必须选的，至少一个self函数
        self.name = name   
        
#通过类创建返回值

p1 = Person('李阳',18)  #创建对象（实例化），参数传递到__init__函数,name和age参数
print p1.name
p2 = Person('王五',16)
print p2.name
'''

#创建一个省的类，对省进行抽象：创建类的目的，对某一类的对象进行抽象
#方法、特性、字段目的是为了让对象处理这一类的请求
#面向对象的公有和私有：外部可以访问和外部不可以访问
class Province():  
    
    #静态字段，属于类
    memo = '中国的23个省之一' #memo是属于类的，memo是没有self的，在类里面声明都属于这个类

    #初始化实例方法
    def __init__(self,name,capital,leader,flag): 
        #动态字段，这些字段只属于这些对象，不能通过类访问，因为动态字段只属于某一个对象，比如hb或者sd
        self.Name  = name #self.Name只属于对象本身
        self.Capital = capital
        self.Leader = leader
        #私有字段
        self.__Thailand = flag   #加下划线，表示为私有字段

    #动态方法，属于对象
    def sports_meet(self):  #省可以开运动会
        print self.Name + '正在开运动会'
        
    #静态方法，属于类  #动态方法变为静态方法，两步操作（1）加装饰器（2）把self去掉

    @staticmethod
    def Foo():
        print '省要带头反腐'
    
    #私有字段只能通过函数间接访问
    def show(self):
        print self.__Thailand
        
    #私有方法
    def __sha(self):
        print '我是alex'
    
    #内部调用私有方法
    def sha2(self):
        self.__sha()
    
    #方法还有类方法，后面再讲
    
    #特性   #把方法改为特性，加装饰器；看起来是方法，但访问是模拟字段的访问
    #特性用处主要是返回值,特性还可以设置为只读和只写
    @property
    def Bar(self):
        print self.Name
        return 'something'
    
    #只读：只能读不能改
    @property
    def Thailand(self):
        return self.__Thailand
    
    #只写：可改
    @Thailand.setter  #装饰器就是函数方法名+setter
    def Thailand(self,value):
        self.__Thailand = value
      
#创建对象，河北
hb = Province('河北','石家庄','李阳',False)
sd = Province('山东','济南','王胜辉',False)

#self是什么？self即是当前创建对象的值，相当于self等于hb，self等于sd，hb和sd就相当于对象【self是python自动传递的】
#类的特性：封装。把name、capital、leader放在类的对象里，打包；封装是为了以后用；
#Name是干什么用的？
#是不是可以加默认参数？

#想看看河北的省会，通过 对象.Capital来访问
print hb.Capital  #self.Capital

#属于类的，通过 类.memo来访问
print Province.memo

#类不能访问动态字段
#print Province.Name这种方式是不可行

#对象可以访问静态字段，hb肯定都属于memo（23个省之一），但尽量不要访问，容易造成歧义
print hb.memo

#调用方法，河北想开运动会
#类里面定义方法，对象就可以调用他
#对象可以访问动态方法，类不能访问动态方法，因为需要实例化
hb.sports_meet()
sd.sports_meet()

#类访问静态方法
Province.Foo()
#对象访问静态方法
hb.Foo()

#特性的访问：看起来是个方法，但访问是通过字段的形式方法
hb.Bar
sd.Bar
print hb.Bar  #打印特性的返回值

#私有字段和私有方法：方法就是函数，属性就是变量
#有些方法不想被外部访问，比如人的心，外面不能调用；只有内部调用，不想暴露给外部
#另外一种是为了安全，不想别人访问你的心，比如一个认证算法，不让其他人访问，只让他们访问接口
#私有字段可以让别人访问，但不能让别人改

#创建对象
japan = Province('日本','东京','小泉',True)

#私有字段的访问
#print japan.__Thailand  通过这种方式访问不到，去过泰国只有自己的身体感觉的到，只有类里面可以访问到
#通过间接的方式访问的到，不能从外部访问,通过中介（类的内部方法）
japan.show()

#私有方法通过外部的方式访问不到 比如japan.__sha()
#也通过间接的方式访问，类内部定义函数
japan.sha2()
print japan.Thailand

#java定义了私有方法，就真的是私有访问，python私有方法默认是不能从外部访问，但也可以调用,方式如下
#一个下划线+类+私有方法 ，但不推荐这么用
japan._Province__sha()


#特性的只读特性和只写特性
#如何操作访问和修改私有字段的访问，先修改为False
japan.Thailand = False
print japan.Thailand