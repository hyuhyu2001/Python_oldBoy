#!/user/bin/env python
#-*- coding: UTF-8 -*-
'''
编写登录接口
-输入用户名，密码
-认证成功后显示欢迎信息
-输错三次后锁定
'''

username_correct = 'king'
password_correct = '123456'

for i in range(3): #3代表循环3次，为0.1.2
    username = raw_input('please enter you name:')
    password = raw_input('please enter you password:')
    if username == username_correct and password == password_correct:
        print '''
            %s,welcome！
            ''' %(username)
        break
    elif i == 2:
        print "你已经输错3次，用户名密码将被锁定"
        break
    else:
        print "你的用户名或者密码错误，请重新输入!你还有%s次机会" %(2-i)
        continue