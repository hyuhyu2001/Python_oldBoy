#!/user/bin/env python
#encoding:utf-8

'''
1、至关重要的__int__.py：有这个才能当做模块使用
2、是否为主文件：__name__
    if __name__ == '__main__' #通过主文件进去
    cmd中：python index.py  #默认index.py为主文件
主文件与从文件的区别
3、查看当前文件路径：__file__
4、查看当前文件描述：__doc__
'''

#导入其他模块的文件，必须有__int__.py  ,这样demo里的函数、变量、方法都可以用
from file import demo
#demo.Foo()  #crtl+左键一键跳转到demo或者Foo函数

print 'module',__name__  #不导入模块时print结果得到__main__
    #导入模块后会打印：demo file.demo  module __main__

#判断是不是主文件，如果是主文件才调用，是从文件不调用
#好处：计算机被攻击了，别人引用主程序执行不了，这里module就是主文件
if __name__  == '__main__':  
    pass
'''
print __file__ #查看当前文件的目录
print __doc__  # 打印注释（模块级别的，开头三个引号的）
'''