#!/user/bin/env python
#encoding:utf-8
from distutils.tests.setuptools_build_ext import if_dl


'''
三层架构之UI层，主程序、主函数
数据访问层
业务处理层
表示层、UI层
尽量把简单的逻辑往上放，把复杂的逻辑往下放
假如对10个语句进行增删改查的话，要写40个，而且数据库连接一直在反复执行。所以通过这个架构写，做了很好的拆解，
对一个表的操作，一下都能看到，后续修改这个表，不用找很多表去更新
'''
from model.admin import import Admin

def main():
    
    user = raw_input('username:')
    pwd = raw_input('password:')
    admin = Admin()
    result = admin.CheckValidate(user,pwd) #调用，验证合法性
    if not result:
        print "用户名或密码错误"
    else:
        print "进入后台管理页面"     

if  __name__ == '__main__':
    main()

