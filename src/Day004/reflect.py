#!/user/bin/env python
#encoding:utf-8

'''
反射第二发
'''

'''
#不用反射的形式去实现
from backend import account  

#输入URL的规范  xxx/xxx，后台函数的存放不可能在一个py文件里，通过不同的py文件做一层区分

#account/login请求登陆操作，指定到登陆的函数中
data = raw_input('请输入地址：')

if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.loginout()
#如果有100个URL，需要写100行，需要改成动态的方式去做，所以通过反射的方式去做
'''
#通过反射的方式去实现，只需要通过5行去实现上述100行的操作
#所有web程序、web框架都是这么做的
#思路是先导入文件夹、再导入模块，最后执行函数
data = raw_input('请输入地址：')
array = data.split('/') #相当于URL中的 / 分割
#print array  结果为 ['account', 'login']

#array[0] = account
userspance = __import__('backend.'+array[0]) #导入模块，+是字符串的拼接
#userspance加入字符串的拼接，相当于下面的导入操作
#from backend import account 
#import backend.account
#backend.account.login()
model = getattr(userspance, array[0]) #相当于上述的导入backend.account.login()，多一步getattr就能完成
func = getattr(model, array[1])

func()

#请输入地址：account/login
#请输入地址：account/logout
#请输入地址：admin/index
#如此便能调用account和admin模块里的函数
