#-*- coding: UTF-8 -*-  

info = 'this var will be printed out...'

name =  raw_input('please input your name:')
job = raw_input('job:')
salary = raw_input('salary:')

real_age=29 #全局变量

for i in range(10): #循环10次，循环次数为0-9，每执行一次，i要加1
    #real_age = 29 
    #每次循环，都在这里声明一次，也是全局变量；只要在函数时才有局部变量
    #不在这里声明，是避免每次猜的时候都调用一次
    age = input('age:')  
    if age>29:   
        print  'think smaller'  
    elif age == 29: #单等号代表声明变量，双等号才是值的比较
        print   'GOOD!10 RMB'  #如何print时打印出颜色？
        break #跳出当前循环
    else:
        print  'think bigger' 
    print 'you still got %s shots!' %(9-i)  #因为第一次循环为0，所以是9-i,必须加小括号，否则按字符串去减

print ''' 
Personal information of %s:
    name:%s
    age:%s
    job:%s
    salary:%s
----------------------------------
'''  %(name,name,age,job,salary)
