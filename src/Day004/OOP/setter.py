#!/user/bin/env python
#encoding:utf-8

'''
特性只写：setter的区别，没有继承object是可读可写的，继承了object默认是只读不可写的，所以必须有setter
'''

class test1:
    
    def __init__(self):
        self.__pravite = 'alex 1'
        
    @property
    def Show(self):
        return self.__pravite 

class test2(object):
    
    def __init__(self):
        self.__pravite = 'alex 2'
        
    @property
    def Show(self):
        return self.__pravite 
    
    #不加setter的话，print t2.Show是无法运行的，因为test2是继承的 test2(object)
    @Show.setter
    def Show(self,value):
        self.__pravite = value 
    
t1 = test1()
print t1.Show
t1.Show = 'change 1'
print t1.Show

t2 = test2()
print t2.Show
t2.Show = 'change 3'
print t2.Show