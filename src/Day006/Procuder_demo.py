#!/user/bin/env python
#encoding:utf-8


'''
面向对象实现生产者消费者模型
多线程能干什么？
生产者消费者模型：有人一直在生产，有一些一直在消费，中间定义一个阀值，保证供需平衡
'''
from threading import Thread
from Queue import Queue
import time

class Procuder(Thread):
    
    def __init__(self,name,queue):
        '''
        @param name:生产者的名字 
        @param queue:容器 
        '''
        self.__Name = name
        self.__Queue = queue
        super(Procuder,self).__init__()
    
    def run(self):
        while True:
            if self.__Queue.full():#容器满了停了不干
                time.sleep(1)
            else:
                self.__Queue.put('bozi') #生产包子
                time.sleep(1)
                print '%s 生产了一个包子' %(self.__Name,)
                #Thread.run(self)


class Consumer(Thread):
    def __init__(self,name,queue):
        '''
        @param name:消费者的名字 
        @param queue:容器 
        '''
        self.__Name = name
        self.__Queue = queue
        super(Consumer,self).__init__()
                
    def run(self):
        while True:
            if self.__Queue.empty():#容器空了就不拿
                time.sleep(1)
            else:
                self.__Queue.get('bozi')  #消费包子
                time.sleep(1)
                print '%s 消费了一个包子' %(self.__Name,)
                #Thread.run(self)
        
#线程安全（队列）：多线程并排着在跑，同时对某一个程序进行处理时听谁的？所以引入锁的功能，某一线程来了锁住，等操作完了，其他线程再来
#队列：先进先出；线程栈是后进先出（比如弹夹最后放的最先出来）

que = Queue(maxsize = 100) #容器：创建队列，设置最大大小

#创建3个线程
baogou1 = Procuder('老狗',que) #创建一个人，一个人就作为一个线程
baogou1.start()  #执行run方法，一直往容器里放包子
baogou2 = Procuder('老狗',que) 
baogou2.start()  
baogou3 = Procuder('老狗',que) 
baogou3.start() 

#创建20个消费者
for item in range(20):
    name = "chenchao%d" %(item,)
    temp = Consumer(name,que)
    temp.start()
    
    
'''
#生产者往容器放东西
que.put('1') 
que.put('2') 

print 'empty:', que.empty() #判断是否为空
print que.qsize()  #看队列里面的大小
#消费者往容器里取东西
print 'get:', que.get() #先进先出，先取1
print 'get:', que.get() #先进先出，再取2 
print 'empty:', que.empty() #先进先出，没有的时候取不到
'''