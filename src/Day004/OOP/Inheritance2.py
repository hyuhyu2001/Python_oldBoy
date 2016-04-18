#!/user/bin/env python
#encoding:utf-8

'''
经典类与新式类的区别
这个例子重现经典类的一个BUG
多继承
'''
from _pyio import __metaclass__
from urllib2 import AbstractBasicAuthHandler

class A:
    def __init__(self):
        print 'this is A'
    def save(self):
        print 'save method from A'
        
class B(A):
    def __init__(self):
        print 'this is B'
       
class C(A):
    def __init__(self):
        print 'this is C'
    def save(self):
        print 'save method from C'
        
class D(B,C):  #从左到右集成，谁在前面先找那个，找不到再找后面的
    def __init__(self):
        print 'this is D'

c = D()
c.save()  
#BUG重现，B没找到，又去了找了A，故永远找不到C
#class A 改为 class A(object)，此BUG便不出现

#多继承是python特有的，java和c#是不允许多继承的
#接口两种含义：（1）别人给你URL，你去调用这个URL（2）定义一个规则，不定义实现，根据规范去写内容

interface IALert  #其他语言支持interface，python不支持
    def send(self):  #发报警短信，必须继承这个接口
        pass

class weixn(IALert):
    def send(self):
        print '微信报警'
    
class Email(IALert):
    def send(self):
        print '邮件报警'
        
#抽象类：降低程序与程序直接的耦合：
#抽象类+抽象方法=接口  （第二种接口：规范）        
#抽象类实例
from abc import ABCMeta,abstractmethod
class Alert:
    __metaclass__ = ABCMeta

    @abstractmethod
    def fun(self):pass
    
class Foo(Alert):  
    def __init__(self):
        print '__init__'
        
    def send(self):
        print 'send.weixin'
        
f = weixin()
f.send()
