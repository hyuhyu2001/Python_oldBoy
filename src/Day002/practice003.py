#-*- coding:UTF-8 -*-
'''
员工信息表
1、用户可以模糊查询员工信息
2、显示匹配了多少条，匹配字符需要高亮显示
'''
#".*"+'%s'%user+".*"
#两个问题（1）模糊查询（2）用户姓名不存在，打印多次

staff = {
    'king':'[山东,33]',
    'xue':'[河南,34]',
    '1king':'[河北,35]',
    'king2':'[北京,36]',
    '3king4':'[武汉,37]',
    'xue5':'[长沙,38]'
}

user = raw_input('请输入你的用户姓名：')

for i in (staff):
    if staff.has_key('%s'%user) is True:
        if i == '%s'%user:
            print i,staff[i]
    else:
        print '用户姓名不存在，请重新输入'
        continue
