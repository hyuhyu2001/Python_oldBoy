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

函数（方法）装饰器
（1）什么是装饰器：装饰器实际就是函数。他接受函数对象，也可以有自己的参数。一般说来，当包装一个函数的时候，会最终调用他。
我们在执行函数之前，可以运行些预备代码，也可以在代码之后做些清理工作。
可以考虑在装饰器中置入通过功能的代码来降低程序复杂度。例如：引入日志，增加技术逻辑来坚持性能，给函数加入事务的能力
（2）装饰器示例：装饰器是在函数调用之上的修饰。这些修饰仅是当声明一个函数或者方法的时候，才会应用的额外调用
@deco2
@deco1
def func(arg1, arg2, ...): 
    pass
#这和创建一个组合函数是等价的。
func = deco2(deco1(func))
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

