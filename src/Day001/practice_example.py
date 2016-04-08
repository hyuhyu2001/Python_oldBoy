#!/user/bin/env python
#encoding:utf-8

#-*- coding: UTF-8 -*-
'''
老师示例
while...else...
'''
import sys
import os
os.getcwd()  #放到0001目录下
#os.chdir('D:\files') #改变当前工作目录，windows不好使？

retry_limit =3 
retry_count = 0 
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

while retry_count < retry_limit: #只要重试不超过3次就不断循环
    
    username = raw_input('username:')
    lock_check = file(lock_file)
    #当用户输入用户名之后，打开lock文件，以检查是否此用户已经lock了
    
    for line in lock_check.readlines():#循环lock文件
        line = line.split()           
        if username == line[0]:  #处理文件，让username精准匹配
            sys.exit('user %s is locked!' %username )#如果lock了就直接退出
    password = raw_input('password:')
    
    f = file(account_file,'rb') #打开账号文件
    match_flag = False #默认为False，如果用户被match上了，就设置为True
    for line in f.readlines():
        user,passwd = line.strip('\n').split()
        #去掉每行多余的\n,并把这一行按空格分成两行，分别赋值为user，passwd两个变量
        #\n就是换行符
        if username == user and password == passwd:
        #判断用户名与密码是否都相等
            print 'Match!',username
            match_flag = True
            break #这里的break只跳出for循环，但没有跳出while循环，break最好不好跳出多个循环
            #相等就把循环外的match_flag变量改变成了True，然后break跳出循环，直接跳出
    f.close()
    if match_flag == False:
    #如果match_flag还未False，代表上面的循环中根本就没有macth上用户名和密码，所以需要继续循环
        print 'user unmatched!'
        retry_count +=1
    else:
        print "welcome login oldboy learning system"
else:
    print 'your account is locked'
    f = file(lock_file,'ab')
    f.write(username) #打开文件，把lock的用户名写入到lock_file文件中，需要换行存储
    f.close()