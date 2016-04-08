#-*- coding:UTF-8 -*-

#什么模式处理文件非常重要
#r以只读模式打开文件，r打开，便不能进行写的操作
"""
f = file('myFile.txt','r')  #打开文件 ,r是以只读的模式打开这个文件,如果不写，则默认是r的模式打开
for line in f.readlines():  #循环这个文件里的每一行，把每一行赋给line变量
    line = line.strip('\n').split(':') #strip（除去，去掉）去掉换行符，split（切割）把这一行按照冒号分割成一个一个的列，再给line赋值
    print line
"""

#w以只写模式打开文件，便不能进行读的操作,w的时候，会直接替换文本里所有的内容,一次操作，可以允许多次write
f = file('myopen.txt','w')    #没有文件时，也可以通过w直接创建文件
f.write(u'中文形式'.encode('utf-8'))  #通过encode可以存入utf-8的形式，python字符集默认存的ASCsII存储，内存里默认是unicode
f.close()

"""
f = file('myopen.txt','r')
print f.encoding  


#a(append)以追加模式打开文件，追加是默认追加到文件的末尾，默认也是不可以读的
f = file('myFile.txt','a')  
f.write('second.line') #不换行操作
f.write('\nthird.line')  #换行操作
f.close()  #即使文件没打开时，也是能够写入，写到缓冲区，也可以强制写入，强制刷新：用f.flush()
"""
#r+以读写模式打开文件:打开文件会保持原文件内容不变，同样可以同时对文件进行读写；可读可写 不会创建不存在的文件 从顶部开始写 会覆盖之前此位置的内容
#w+以写读模式打开文件：写读是清空这个文件再往里写，打开文件会将原文件内容删除，可以同时对文件进行读写
#a+以追加读模式打开文件：可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建

#建议用下面+的方式
#r+b二进制的模式去处理文件，在windows有用，linux没用。linux换行符是\n，windows的换行符是\n\r  二进制处理时会自动把windows的换行符转换为linux
#w+b二进制的模式去处理文件
#a+b二进制的模式去处理文件