#-*- coding:UTF-8 -*-
'''
要求用户输入工资，然后打印购物菜单
用户可以不断的购买商品，直到钱不够为止
退出时格式化打印用户已购买的商品和剩余余额
'''
import sys

dict_shop = {
    'bike':'10',
    'car':'20',
    'food':'5',
    'water':'3',
    'house':'1000'
}
shopping_cart = [] #定义一个空列表，作为购物车列表

salary = input('please enter your salary:')
balance = salary #变量放外面，循环时就不会读取了


while True:  #for i in (dict_shop),循环次数只按字典里的集合数循环，故这么写最多循环5次,故用while True表示永远执行
    if balance > 0:
        print '以下是你要购物的清单'
        print '------------------------'
        for i in dict_shop:  
            print i, dict_shop[i] 
        print '------------------------'
        
        item =  raw_input('你的余额为%d,请输入你要购买的商品:' %balance)   
        buy =  int(dict_shop.get('%s'%item))
        balance -= buy #通过变量可以在print里计算结果，需要把每次循环的金额算进来
        if balance >= buy: #当商品金额大于余额时，不允许购买商品
            shopping_cart.append('%s' %item)  #已购买的商品，记录到购物车里面，后续可以打印列表（即打印购物车）
            print '''
                    你已购买商品为 %s
                    你的余额还剩%d：
            ''' %(shopping_cart,balance)
            choice = raw_input('是否继续购买？(y/n)')
            if choice == 'n':
                print '谢谢惠顾，欢迎下次光临！'
                break
            else:
                continue
        else:
            print '购买商品价格已超出余额，请重新购买'
            break
    elif balance == 0:
        print '你的余额为0，不能继续购买'
        break
    else:
        print '你的余额已经不足，请退出'
        sys.exit()

    