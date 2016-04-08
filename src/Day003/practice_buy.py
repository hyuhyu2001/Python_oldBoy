#!/user/bin/env python
#encoding:utf-8


dict_shop = {
    'bike':'10',
    'car':'20',
    'food':'5',
    'water':'3',
    'house':'1000'
}

shopping_cart = [] 
Payment_amount = 0

while True:
    print '以下是你要购物的清单'
    print '------------------------'
    for i in dict_shop:  
        print i, dict_shop[i] 
    print '------------------------'
    item =  raw_input('请输入你要购买的商品:' )   
    buy =  int(dict_shop.get('%s'%item))
    Payment_amount += buy
    shopping_cart.append('%s' %item) 
    print '''
            你已购买商品为 %s,
            总共需要付款%d：
        ''' %(shopping_cart,Payment_amount)
    choice = raw_input('是否继续购买？(y/n)')
    if choice == 'y':
        continue
    elif choice == 'n':
        print '''
                你已购买商品为 %s,
                总共需要付款%d：
            ''' %(shopping_cart,Payment_amount)
        break
