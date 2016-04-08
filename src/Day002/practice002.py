#-*- coding:UTF-8 -*-
'''
员工信息表
1、用户可以模糊查询员工信息
2、显示匹配了多少条，匹配字符需要高亮显示
'''
#疑问：界面输入的中文，咋打印为乱码，字符串如何转换


staff = {
    '张三':'[山东,33]',
    '李四':'[河南,34]',
    '王五':'[河北,35]',
    '高六':'[北京,36]',
    '高六':'[武汉,37]',
    '一高六八':'[长沙,38]'
}

user = raw_input('请输入你的用户姓名：')
print type('%s'%user)
user = ('%s'%user).decode('UTF-8')
print user
print '%s'%user.encode('UTF-8')  
for i in (staff):

        print i,staff[i]
