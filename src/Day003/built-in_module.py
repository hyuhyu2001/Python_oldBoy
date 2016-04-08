#!/user/bin/env python
#encoding:utf-8


import random  #为什么导入时报错？待解决

'''
#生成随机验证码,一个random模块，3个函数
print random.random()  #生成一个随机数
print random.randint(1,5) #在1和5（>=1，<=5）之间随机生成一个整数
print random.randrange(1,10) #在1和10之间（>=1，<10）
'''

#随机数的思路，比如生成六位数，六位数可以有字母有数字,1位1位生成
temp = random.randint(65,90)#生成随机数字
print chr(temp) #获取大写字母 

code = []

for i in range(6):#0-5，6个数，进行6次循环
    if i == random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
        #code把字符添加到一个列表里
print  ''.join(code)#把列表格式化到字符串里,最终生成一个随机数
#join与+=的区别，join效率最高，+=每次都次请求都会开辟一个空间，但join只需开辟一次即可

#其他列子
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print checkcode
