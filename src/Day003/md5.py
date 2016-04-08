#!/user/bin/env python
#encoding:utf-8

'''
明文存密码不可以，需要加密，md5便是加密的手段
'''

#import md5,官方不推荐使用

import hashlib #模块下有好多加密方式，md5是其中一种
hash = hashlib.md5() #创建了一个对象
hash.update('admin')
print hash.hexdigest()  #加密之后，16进制
print hash.digest()   #hexdigest与digest区别主要是长度

#加密是存入，登陆时怎么判断密码是否一样
#md5是不能够反解的，用书输入时，对输入的值，再次进行md5加密，然后与数据库进行判断
#每次加密都是一样的值