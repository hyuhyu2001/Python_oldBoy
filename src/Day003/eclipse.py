#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''
1、为什么用IDE
输入一个字符自动出全部
python提供了很多模块，只需调用
eclipse直接看源码
代码分到不同的模块，相同的模块放到同一个功能
代码与数据分开，模块与模块分开
提升B格的：反射和装饰器
2、eclipse使用步骤
（1）创建工作空间workspace
（2）创建工程：Project：PyDev Project：右键可以关闭工程，可以打开工程
（3）/python-lib：可以查看python源代码
（4）pydev package（包）：
   a、  __int__.py 自动生成此文件（  新建file时没有此文件）
   b、邮件可以copy “__int__.py”，复制到file，file会变为package
       要想引用：from file import demo，必须是包才能导入模块，直接file的无法导入
   c、创建头文件模板
（5）邮件创建pydev module（文件）；
 (6)双击行的前面，打断点:breakpoint;目的是为了调试，就无需用print调试，直接用debug as（苍蝇）调试
在断点时不操作的话走的时候，不会往下走
debug-弹窗（勾选）-点小箭头（resume F8）-两种调试窗口
或者按红点暂停
（7）很多函数时择起来，从右侧可以直接看到：
outline咋出来：windows-show view-ouline
拖拽可以调整调试窗口的位置
console：输出
全局的编码windows-preferences-general-editors-spelling-更改编码
某一个工程也可以设置编码
全局的优先级<工程的<某一个文件
（8）通过ctrl+左键在多个文件里跳转
    函数加注释也能直接看到
'''

name  = 'alex'

actione= 'doubi'

print name
