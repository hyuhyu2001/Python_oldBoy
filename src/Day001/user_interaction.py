#-*- coding: UTF-8 -*- 
#user interaction 用户交互

#name = 'alex'
#print "my name is "+name+" haha" #两个加号表示字符串的变量

info = 'this var will be printed out...'

name =  raw_input('please input your name:')
age = input('age:')  
job = raw_input('job:')
salary = raw_input('salary:')

print type(age)

#格式化打印，多行打印
print ''' 
Personal information of %s:
    name:%s
    age:%s
    job:%s
    salary:%s
----------------------------------
'''  %(name,name,age,job,salary)


'''
用户交互
输出格式化：
    询问用户姓名，年龄，性别，工资
    以格式的方式输出
用3个引号，可以print多行
%s代表字符串，
%d代表数字
%f代表浮点数
【所有用raw_input()输入的默认都是字符串，所以都要用%S】
如果想要转换为数字，则 age = int(raw_input('age:'))  还可以直接用input
输入age时，如果输入'39'，则表示输入的是字符串
raw_input与input都是通过读取控制台的输入与用户实现交互
区别如下：raw_input只能输入的是字符串;input原生格式是什么，就调用什么（可以是字符串、数字、甚至是变量）
'''