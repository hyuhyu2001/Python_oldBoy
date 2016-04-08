#-*- coding: UTF-8 -*-  

info = 'this var will be printed out...'

name =  raw_input('please input your name:')
age = input('age:')  
job = raw_input('job:')
salary = raw_input('salary:')

print type(age)

if age>40:   #输入41的时候，虽然既>40，也>30,只打印第一个，满足第一个条件时跳出循环
    msg = 'You are too old!'  #赋值变量，最后print统一打出
elif age>30:
    msg = 'you still have a few years to xx up'
else:
    msg = 'you are still young' #必须用同一个变量，否则最后打印时需要打印两个变量

print ''' 
Personal information of %s:
    name:%s
    age:%s
    job:%s
    salary:%s
----------------------------------
%s
'''  %(name,name,age,job,salary,msg)
