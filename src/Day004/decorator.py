#!/user/bin/env python
#encoding:utf-8

'''
装饰器，提升B格的另一利器
'''
from robot.result.executionresult import Result

'''
下面有一万个函数
产品需求1：在Func1、Func2、Func3....前面都加一个验证 
产品需求2：在Func1、Func2、Func3....前面加的验证都去掉 
产品需求3：在Func1、Func2、Func3....前面加验证再换个方式实现以下 
'''

#通过断点，跟踪装饰器的解释过程
#通过装饰器改变，装饰器也是一个函数，如下:装饰器是为了装饰函数的
#函数加参数如何处理
#函数加返回值如何操作
def outer(fun):
    def wrapper(arg):     #arg为，为装饰器增加函数参数
        print '验证'  #新提的需求，加验证
        result = fun(arg)   #arg为，为装饰器增加函数参数 ，result为接收原函数的返回值
        print '嘻嘻嘻' #新提的第二个功能 
        return result   #为返回值增加一个return
    return wrapper


@outer  #通过outer把函数和装饰器进行关联，outer为装饰器的函数名，相当于 @outer = outer(Func1)
def Func1(arg):
    print  'Func1' ,arg 
    return 'return'

#通过装饰器，相当于对Func1()又做了一个复制，相当于func1 = wrapper函数；fun()就是原来func1的传参
Func1('alex')  #客户端增加一个参数
response = Func1('alex')   #获取返回值，返回的原函数的return的值
print response  

