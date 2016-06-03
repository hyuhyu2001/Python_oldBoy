#!/user/bin/env python
#encoding:utf-8


'''
process（进程）
thread(线程)
程序操作某个业务需要进程和线程，一个程序可以有多个进程，一个进程里面可以有多个线程
CPU:中央处理器，处理用户发来的请求，
（1）以前时聊天和听歌不能同时进行，原始是单线程排队处理
（2）后面出来分片技术（一次执行1秒钟，执行这个线程1秒钟再执行其他线程,用户会感觉三个程序是同时进行），但同一时刻只有同一线程执行
（3）多个CPU：同一时刻可以同时执行两个线程，每个应用程序可以有多个线程
一个物理CPU可以分几盒，目前物理CPU可以达到18盒，逻辑CPU可以达到36盒，一个进程可以在多个CPU跑不同的线程
python中有全局解释器锁，同一时刻内只能出来一个线程，感官上python比其他语言慢，去掉锁后效率比有锁慢
（4）解决慢的方案：多进程处理，同一时刻可能会有两个进程处理，出现问题（进程和进程的资源共享问题，会浪费内存）
什么时候用多进程？计算密集型通过CPU计算，选择多进程
什么时候用多线程？IO密集型不用一直占用着CPU，选择多线程
多进程时每个进程可以多线程么？都是由程序员决定
'''
'''
threading比Thread模块更高级
'''

#创建线程和执行线程，最基础的
from threading import Thread
import time
#非常耗时的线程，比如：
def Foo(arg,v):
    for item in range(10):
        print item
        time.sleep(1)

print 'before'
t1 = Thread(target=Foo,args=(1,11,)) #创建线程
#print t1.isDaemon()  守护线程默认是False
t1.setDaemon(True) #start之前规定是否为守护线程，如果主线程一直没有结束，子线程会执行；主线程执行完之后，子线程不执行
t1.start() #运行时有可能执行
t1.join(5) #主线程到达join之后便不执行，等到子线程执行完后再执行，如果设置timeout，则为最多等待时间，等待5秒后执行主线程
print t1.getName()
print 'after'
print 'after'
print 'after'
print 'after end'

#创建线程没有限制，每个线程有上下文，程序是因为上下文切换的时候浪费资源

'''
Thread模块中的方法
start
getName() 获取线程名称
setName() 主动设置名称
isDaemon() 守护线程：默认执行主线程，子线程执行慢的话最后也会执行
setDaemon()
join(timeout)主线程到达join之后便不执行，等到子线程执行完后再执行，如果设置timeout，则为最多等待时间，等待5秒后执行主线程
run() 通过run方法来执行指定的函数,程序默认有run方法执行，可以通过run函数来改变
'''



     
