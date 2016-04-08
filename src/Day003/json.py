#!/user/bin/env python
#encoding:utf-8

'''
序列化和json，以及区别
序列化：可以把一个对象（列表、字段）通过python特有的机制，给序列化一下，特殊二进制给加密一下，序列化后可以反序列化
json：接口json格式（或者xml，目前用的少），json就是标准化的数据格式，把内存里的数据进行序列化（json话）
序列化和json区别：
（1）pickle只能在python用，json是所有语言都支持的数据格式
（2）pickle不单可以dump常规的数据类型，也可以去序列化类、对象（python所有的数据类型），json只能序列常规的数据类型（字典、列表、集合），因为不同语言语法不一样
（3）pickle序列化数据是人不可读的，json序列化数据是人能直接看到数据的

import pickle

li = ['alex',11,22,'ok','sb']
dumpsed =  pickle.dumps(li)  #通过dumps进行序列化，无规则
print dumpsed
print type(dumpsed) #列表序列成字符串的形式
loadsed = pickle.loads(dumpsed)#反序列化
print loadsed
print type(loadsed) #有转变为list

#序列化场景：用户名存文件，读进来再进行拼接，序列化可以直接序列化到文件中，以后可以读取这个文件，再反序列化这个文件
#场景：python与python之间的文件传输，1个人序列化文件，另外1个人读取文件
#为啥共享文件？两个python文件内存数据的交互，两个独立的进程在内存里，内存是独立的，两个内存默认是不能访问的；两个程序想进行数据的交换
#因为存在父与子的关系不能直接数据，非常复杂的字典非常轻松的让他们程序调用，实现两个内存里数据的交互
#pickle序列表不止字典、内存，也能把整个类存进去，比如游戏里把状态记录下来（内存数据又回来了，把内存数据dump到硬盘中）
#socket编程，socket只能传字符串和二进制，怎么把服务端数据传给客户端用，必须得把列表序列化，然后到客户端再反序列化
pickle.dump(li,open('D://dump.txt','w'))#序列化到文件中,dumps直接生成字符串，dump生成文件
result = pickle.load(open('D://dump.txt','r'))#从文件里读出来:load
print result
'''

#json：接口json格式（或者xml，目前用的少），json就是标准化的数据格式，把内存里的数据进行序列化（json话）
#存储同样的信息量，xml耗费空间比json要大很多，xml比较复杂
import json
name_dic = {
    'name':'wupeiqi',
    'age':23
    }
print json.dumps(name_dic)  #为什么报错？
