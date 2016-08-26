#!/user/bin/env python
#encoding:utf-8

'''
多线程开发之事件
两个线程都会监测一个变量
'''
import threading
import time

def producer():
    
    print u'chef:等人来买包子。。。' #顺序01
    event.wait() #Flag变成True，wait变没了，直接往下走
    event.clear()  #这里必须清除第一个set，否则第二个set的顺序就错了

    print u'chef:sb is coming for bozi...'
    
    print u'chef:making a bozi for sb...'
    time.sleep(3)
    
    
    print 'chef:you baozi is ok'
    event.set()

def consumer():
    print u'chenchao:buy bozi'
    event.set() #把flag变成True
    
    time.sleep(2)
    print 'chenchao:waiting for baozi to be ready'
    while True:
        if event.isSet():#判断set是否为True
            print  u'reading'
            break
        else:
            print u'还没好啊'
            time.sleep(1)
    
    print event.wait() 
    
#怎么告诉别人我来买包子，通过事件触发
event = threading.Event()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()