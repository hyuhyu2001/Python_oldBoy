#!/user/bin/env python
#encoding:utf-8

str1 = 'reflect001'
str2 = 'Foo'

module = __import__(str1)  # 等于 import demo，导入模块

func = getattr(module, str2)  #从模块里获取函数  ,得到一个返回值
#得到的返回值便是函数 def Foo():

func()

##根据url的不同，返回不同的结果