#!/user/bin/env python
#encoding:utf-8

'''
线程和进程的区别？
（1）进程产生线程，线程是CPU的最小执行单元；
（2）线程是共享内存（属于进程下面管理，共享主线程内存空间），进程不共享
10个线程都要同时修改一个数据的时候，每个线程给变量加1
（3）线程没有办法单独运行
修改之前先确认这个变量有没有被别人锁住；
'''
import threading
import time

'''
num = 0 #声明全局变量

def run(n):

    time.sleep(1)
    global num#需要global一下
    lock.acquire() #独占这个CPU的操作，获得这个锁，锁只放到操作的时候
    num += 1 #两num的变量不一样，这里是局部变量,局部变量不能直接改全局变量的值


    lock.release() #释放这个锁
    time.sleep(0.01) #同一时刻只有一个线程在执行，sleep时便不等待
    
    print '%s\n' %num #加入换行 #放在外面时就会抢线程，导致有重复的数字出现

#run('dd')
#print num

lock = threading.Lock() #建锁

for i in range(100): #启动100个线程
    t = threading.Thread(target=run,args=(i,))
    t.start()
'''   
'''
num = 0 #声明全局变量

num2 = 0 

def run(n):

    time.sleep(1)
    global num
    global num2
    lock.acquire() 
    num += 1 
    lock.acquire()  #特殊情况下需要获得好几把锁
    num2 += 2

    lock.release() #释放这个锁
    lock.release() #释放num2的锁，但程序不知道释放的哪个锁
    time.sleep(0.01) 
    
    print '%s\n' %num #


lock = threading.RLock() #Rlock允许同时获得好几把锁，可以记住一个数组程序，当自己用锁时会计数，释放琐时需要释放两次
#samp = threading.BoundedSemaphore(2)#允许最大连接数：同一时刻允许几个人上厕所，比如两个坑

for i in range(100): 
'''    
    
num = 0

def run(n):

    time.sleep(1)
    global num
    samp.acquire() 
    time.sleep(0.001) 
    num += 1 
    print '%s\n' %num 
    samp.release() 

    
samp = threading.BoundedSemaphore(4)#允许最大连接数：同一时刻允许几个人上厕所，比如两个坑

for i in range(100): 
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t = threading.Thread(target=run,args=(i,))
    t.start()

