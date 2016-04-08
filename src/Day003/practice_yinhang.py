#!/user/bin/env python
#encoding:utf-8

'''
网上银行，
功能（必须）
1、额度 15000，初始化，给他15000
2、可以提现，收费5%
3、每月最后一天出账单（每月30天），写入文件
4、记录每月日常消费流水
5、提供还款接口 优化（还款和其他功能分开，给别人一个接口）
可选
1、每月10号位还款日，过期未还，俺欠款额5%计息
其他功能：密码输错3次，账户锁定；

'''
import sys
#import pickle

#登陆函数，用户名与密码的校验，以及操作的返回在这里
def login(cardID,password):
    cardID_correct = '987'
    password_correct = '123'
    for i in range(3): #3代表循环3次，为0.1.2
        cardID = raw_input('please enter you cardID:')
        password = raw_input('please enter you password:')  
        if cardID == cardID_correct and password == password_correct:
            print '''
                %s,欢迎，你已经登录成功，你能进行如下操作！
                ''' %(cardID)
            return 'success'
        elif i == 2:
            print "你已经输错3次，用户名密码将被锁定"
            break
        else:
            print "你的用户名或者密码错误，请重新输入!你还有%s次机会" %(2-i)
            continue

#定义函数之间调用
def main(cardID,credit,balance):
    operation_res = operation(cardID,credit,balance)
    if operation_res == '1':
        withdrawals(cardID,credit,balance)
    elif operation_res == '2':
        query(cardID,credit,balance)      
    elif operation_res == '3':
        repayment(cardID,credit,balance)
    elif operation_res == '4':
        shopping (cardID,credit,balance)
            
            
#功能列表：登陆后可进行什么的操作
def operation(cardID,credit,balance):
    dict_yinhang = {
        '1':'提现：不能超过限额，手续费5%',
        '2':'查询：查询余额和交易明细',
        '3':'还款：现金还款',
        '4':'转账：可转账至不同账户',
        '5':'退出'
    }   
    print '你的额度为%s，你的剩余额度为%s'%(credit,balance)
    print '------------------------'
    for i in dict_yinhang:  
        print i, dict_yinhang[i] 
    print '------------------------'
    while True:
        choice = raw_input('请输入你要进行的操作：')
        if choice == '1':
            return  '1'
        elif choice == '2':
            return  '2'
        elif choice == '3':
            return '3'    
        elif choice == '4':
            return '4'        
        elif choice == '5':
            print '谢谢光临'
            sys.exit()
        else:
            print '请按提示的数字输入操作'
            continue

#提现不能超过限额，每次手续费5%    
def withdrawals(cardID,credit,balance):
    crash = 0
    while True:  
        crash = input('你剩余的额度为%s请输入你要提现的金额：'%balance)
        if crash*1.05 <= balance:
            print '提现成功，本次取钱%d，手续费为%d，你剩余的金额为%d'%(crash,crash*0.05,balance-crash*1.05)
            crash = crash*1.05
            balance -= crash
            #detail = pickle.dumps(crash) 交易流水如何做
            crash_choice = raw_input('请确认是否继续提现？(y/n)')
            if crash_choice == 'n':
                print  '谢谢光临，请继续其他操作' 
                break
            else:
                continue
        else:
            print '你的余额已经不够，请重新输入金额'
            break
    main(cardID,credit,balance)

#查询操作，查询余额和交易明细
def query(cardID,credit,balance):
    print '你的额度为%d,剩余的额度为%d'%(credit,balance)
    query_choice = raw_input('查询完毕，是否返回主菜单(y/n)' )
    if query_choice == 'y':
        main(cardID,credit,balance)
    else:
        print '欢迎光临！'
        sys.exit()
    
def repayment(cardID,credit,balance):
    print '你的额度为%d,剩余的额度为%d'%(credit,balance)
    repay_crash = 0
    while True:
        repay_crash = input('请输入你要还款的金额:')
        balance += repay_crash
        print '还款成功，你的可用额度为%d，还剩%d未还'%(balance,credit-balance)
        repayment_choice = raw_input('请确认是否继续还款？(y/n)')
        if repayment_choice == 'n':
            print  '谢谢光临，请继续其他操作' 
            break
        else:
            continue
    main(cardID,credit,balance)
        
def shopping (cardID,credit,balance):
    print '购物'


cardID = ''
password = ''
credit =15000
balance = credit
#detail = ''

if __name__ == '__main__':
    main()
    
login_res = login(cardID,password)
if login_res == 'success':
    main(cardID,credit,balance)


