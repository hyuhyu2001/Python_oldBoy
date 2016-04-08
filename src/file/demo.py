#!/user/bin/env python
#encoding:utf-8
'''
函数是功能的封装
'''
#from file import demo
print  'demo',__name__  #运行打印也是__main__

def Foo():
    '''中文介绍
    '''
    bar()
    print '老狗去砍柴'
    
def bar():
    '''中文介绍
    '''
    #调用其他900008个函数
    print '老狗去砍柴'
    
#为了防止其他人调用主函数，会执行所有程序，这个时候就用__name__
if __name__ == '__main__' :  #__main__就是表示直接直接执行，而不是别人调用，控制主文件不被其他人调用
    Foo()  #调用父函数，父函数再调用其他函数
else:
    print '滚'


    
