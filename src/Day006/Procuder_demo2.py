#!/user/bin/env python
#encoding:utf-8

'''
函数式编程实现生产者消费者模型
生产者消费者最大特点：为了解耦，解耦就是让程序各个模块之间关联性降到最低
买包子，但是需要等指定厨师做包子，这样便产生了阻塞
但有收银员（Queue，消息队列）后，客户不关心哪个厨师做包子，厨师不关心哪个客户买，这个便是非阻塞模式（支持并发，支持忙闲不均）
再高级一点，客户不用等5分钟，等我做好了包子，我告诉你（即是异步模型）
'''
import threading,time,Queue #不规范写法，正常需要些3行
import random

def Proudcer(name,que):
    while True:
        if que.qsize()<3: #队列小于3个的时候生成包子
            que.put('baozi')
            print '%s:Made a baozi...' %name
        else:
            print '还有3个包子'
        time.sleep(random.randrange(1)) #在1秒内取一个随机数,通过时间随机造成忙闲不均

def Consumer(name,que):
    while True:
        try:
            que.get_nowait('baozi')  #造成不阻塞，没有包子时会报错，线程全端
            print '%s:Get a baozi...' %name
        except Exception:
            print u'没有包子了...'
        time.sleep(random.randrange(3))
    
q = Queue.Queue()
p1 = threading.Thread(target = Proudcer,args = ['chef1',q])
p2 = threading.Thread(target = Proudcer,args = ['chef2',q])
p1.start()
p2.start()

c1 = threading.Thread(target = Consumer,args = ['chenchao1',q])
c2 = threading.Thread(target = Consumer,args = ['chenchao2',q])
c1.start()
c2.start()


