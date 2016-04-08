#!/user/bin/env python
#encoding:utf-8

'''
1、函数只有在运行时才会执行，必须有入口 比如 foo()
只能指定一个父函数
2、函数式编程、函数结构
参数             def Fun(arg,*args,**kargs):
默认参数             print arg
可变参数            print args
                 print kargs
返回值              return 'sucess'
3、一批功能封装到一起,把相同的工作放在一起，建议一个大功能不超过一屏
函数可以当做模板
功能拆分成函数：比如买东西函数，购物车函数，结果函数，把代码分解
4、函数有参数，有返回值
5、return返回值：让别人干一件事，最后得通知我是否干成，要一个回馈或者返回信息
让函数干一个事，函数给我一个结果
'''
'''
#设置默认参数必须把默认值的参数放到最后面，不能def foo(action='砍柴',name)这么写
def foo(name,action='砍柴',where='北京'): #action='去砍柴'，为action设置默认值
    print name,'去',action,'在',where #name是变量

foo('liyang','砍柴',)
foo('laogou','吃饭')
foo('alex','xx')
foo('zhang',where='上海')  #没定义action，会取默认参数;;;中间省略的话，需要把行参的名字放前面（where）
foo('heibei',where='上海',action='oo') 

#把登陆功能分解
def login(username):
    if username == 'alex':
        return '登陆成功'
    else:
        return '登陆失败'

#登陆详细
def detail(user):
    print user,'XXXXXXXXXX'
        
if __name__ == '__main__':
    user = raw_input('请输入用户名：')
    
    res = login(user) #调用函数，检查用户是否合法；
    #res定义为返回后接收一个返回值
    if res == '登陆成功':
        detail(user) #显示详细
    else:
        print '没奖金了' 
'''
'''
def show1(arg):
    for item in arg:
        #各种炫酷效果
        print item
        
def show2(arg1,arg2):
    print arg1,arg2
    
show1(['lyang','alex']) #第一次传列表的参数
        
show2('liyang','zhangbin')    #第二次传两个字符

#参数长度不定，就加一个*，这样会把参数包装成一个列表
def show(*arg):  #带*，参数可以输入很多很多,最后把参数转换为列表传入到函数中
    for item in arg:
        print item

show('liyang','zhangbin','liyang','zhangbin','liyang','zhangbin','liyang','zhangbin','liyang','zhangbin','liyang','zhangbin')
'''    

#参数长度不定，就加两个*，这样会把参数包装成一个字典 
def show(**kargs):
    for item in kargs.items():  #封装，包装成一个字典
        print item 

show(name='liyang',age= 'zhangbin') #会把name当成key，age当成value

user_dict ={
    'k1':'123',
    'k2':456        
}

show(**user_dict)  #字典当参数的话，必须加两个*号传入

#元组和集合是一个*