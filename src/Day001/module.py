#-*- coding: UTF-8 -*- 

import os
os.system('pwd')

import commands

import sys
print sys.argv
print sys.argv[2]


from sys import argv
print argv

import multiprocessing as multi
from sys import *

'''
什么是模块：如果你想要在其他程序中重用很多函数--定义模块
python是由一系列模块组成，每个模块就是一个py为后缀的文件，同时模块也是一个命名空间，
从而避免了变量命名冲突的问题。模块我们就可以理解为lib库，如果需要使用某个模块的函数或者对象
则要导入这个模块使用才可以，除了系统模块（内置函数）不需要导入
1、模块内有很多函数方法
2、模块可以在文件中永久保存代码
3、模块可以跨平台使用，只要copy代码就行
怎么使用现成的模块，4种导入方法
1、import sys 是整个模块都导入 （不需要加py后缀）
2、from sys import argv  ，后面打印时可以直接输入 print argv
3、import multiprocessing as multi 通过as起别名
4、from sys import *：把sys模块下的所有方法都导入进来，print path ；
    不建议使用，因为可能会和变量冲突，所以输入前通过模块名调用是做好的，不会和已知的变量重名
    对于每个模块的导入，

python解释器只会导入一次，即使重复使用import和from…import语句，也只有在PVM检测到该模块没有被导入时才执行导入动作。
即使后来你修改了模块的源代码，但没有重启PVM，python解释器仍然是使用之前导入的内容在处理。
如果需要重新载入修改后的源码，一是退出python的交互模式后再进入，二是直接使用reload语句
'''