#!/user/bin/env python
#encoding:utf-8
'''
error
'''
'''
data = raw_input('请输入地址：')
array = data.split('/') 

#捕捉异常用try
try:
    userspance = __import__('backend.'+array[0]) 
    
    model = getattr(userspance, array[0])
    func = getattr(model, array[1])
    
    func()
    
#多个error用小括号扩展
except ImportError,e: #e 代表ImportError 这个对象 （ImportError,没有这个模块）
    print 1,e    #e就是到底出了什么错；No module named eee  
    print '自定义404'
    #对错误类型进行制定，可以分开写
except AttributeError,e:  #AttributeError，模块里没这个属性  报错信息：module' object has no attribute '111'
    print 2,e    #e就是到底出了什么错；No module named eee  
    print '自定义404'
#如何囊括所有error？
except Exception,e: 
    print 3,e    
    print '自定义404'
    
#没有出错时，可以else操作
else:
    print '没有出错'
    
finally:
    print '无论异常与否，都会执行'  #有错误也会执行，没错误也会执行
   

合并写
except (ImportError,AttributeError),e: #e 代表ImportError 这个对象 （ImportError,没有这个模块）
    print e    #e就是到底出了什么错；No module named eee  
    print '自定义404'

'''
#上面都是用python的异常，如何自定义异常呢？通过类的方式，继承Exception

class MyException(Exception):
    
    def __init__(self,msg):
        self.error = msg
    def __str__(self,*args,**kwargs):   #str功能：一旦类里面重写了str方法，以后print会输出str返回的值（返回str输出的字符串）
        #return '该对象是MyException类实例化的一个对象'
        return self.error
    
obj = MyException('自定义错误信息')  #return self.error，则print obj时会返回obj定义的错误信息
print obj   #输出'该对象是MyException类实例化的一个对象'；假如没有__str__时，则print时没有值输出

raise MyException('自定义错误')  #手动触发一个自定义错误的异常

#为什么主动触发一个异常，如下：

def Validate(name,pwd):
    
    if name == 'alex' and pwd == '123':
        return True
    else:
        return False
try:
    res = Validate('alex','456')
    if res:
        print '登陆成功'
    else:
        #print '记录日志到数据库'  #一旦有error便记录到数据库，很多地方会很多操作
        #print '登陆失败'
        raise Exception('登陆失败')  #主动触发，会巧妙的去掉不少冗余代码
except Exception,e:    
    print '记录日志到数据库'
    print e


