#!/user/bin/env python
#encoding:utf-8

'''
类的继承：父亲的东西，可以继承
1、可以继承  2、可以进行修改
'''

#父类（基类），子类（派生类）
            
class Father(object):  
    
        def __init__(self):
            self.Fname = 'fffff'
            
        def Func(self):
            print 'father.Func'

        def Bad(self):
            print 'father.抽烟喝酒烫头'
                      
class Son(Father):  #子类继承父类，即是建立了子类和父类的关系  
    #可以继承两个，class Son(Father,uncle)
    
        def __init__(self):
            self.Sname = 'sssss'
            print 'son.__init__'
            Father.__init__(self)  #调用父类的构造函数
            super(Son,self).__init__()  #通过这种方式也可以调用父类的构造函数:需要父类继承object，son加参数self
             
        def Bar(self):
            print 'son.bar'
        
        '''
        def Bad(self): #继承之后，重写父类的方法
            print 'son.抽烟喝酒'
        '''  
        def Bad(self):
            Father.Bad(self) #父类的方法直接继承
            print 'son.赌博'   #继承父类，然后进行很少的加工，不能直接修改父类，因为父类会有很多子类
            
#创建一个儿子（实例化），有些东西继承父亲的

s1 = Son() #创建一个儿子
s1.Bar()
s1.Func()  #继承了父类，可以直接执行

#子类继承父类，可以继承过来然后重新定义
s1.Bad()

#类如果继承object则叫新式类，如果不继承object叫经典类，比如 class Father(object):
#新式类比经典类多一些东西：比如__name__;__doc__;python2.2增加新式类，兼容经典类（优化BUG:经典类继承多个类的BUG）
#新式类和经典类用哪个？大牛用的都是新式类：原因是原先的python是函数式编程，后面往面向对象发展，发展过程中出现object类
#object类是所有类的祖宗，object是调用C的接口
#类可以进行多继承：子类继承父类、父类继承父父类，父类和父父类都有一个相同的方法
#继承两个优先：一个深度优先，一个广度优先
#继承顺序