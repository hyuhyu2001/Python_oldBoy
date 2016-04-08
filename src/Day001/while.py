#-*- coding: UTF-8 -*- 

#print_num = input('which loop do you want it to be printed out?')
#一样的代码不要有重复，效率低，可以定义函数，没函数时而如何实现
import sys

print_num = 0 #技巧性令初始值为0，则能走入循环里的print_num
count = 0
while count<1000000:
    if count == print_num:
        print 'there you got the number:', count
        while print_num <= count:
            print_num = input( 'which loop do you want it to be printed out?[input 0 to exit]')
            if print_num == 0:
                sys.exit('exit the program')
            if print_num <= count: #因为上面有print_num便会打印，所以加if
                print u"已经输入过了！"
            
    else:
        print 'Loop:',count

    count +=1
else:
    print 'loop:',count

'''
whilie不指定条件的话，便是死循环
python有while...else...的用法
linux和windows中，tab键默认的缩进不一样，linux是tab键，windows缩进默认是4个空格
'''
