#!/user/bin/env python
#encoding:utf-8

from threading import Thread
import time

#自定义线程
#继承Thread，在原有基础上增加新的功能
class MyThread(Thread):
    
    def run(self):
        time.sleep(5)
        print '我是线程'
        Thread.run(self) #调用了父类的run方法
        
#默认的t1 = Thread(target=Foo,args=(1,11,)) 

def Bar():
    print 'bar'

    
t1 = MyThread(target=Bar) #通过target传给run方法，会执行从Thread中传过来的构造函数__init__
t1.start()
print 'over'
