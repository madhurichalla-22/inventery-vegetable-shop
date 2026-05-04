#vegetable shop billing system
items=['brinjal','tamota','onion','mirchi','cabbage','potato','ladies finger','radish',
       'cauliflower','beans','cucumber','drumsticks','capcicum']
prices=[65,30,20,40,65,35,30,70,50,80,55,75,55]
quantitys=[50,30,40,25,45,70,80,20,25,40,70,10,25]
cost_prices=[60,26,15,37,60,30,28,68,49,77,54,73,52]

cart_item=[]
cart_qty=[]
cart_amount=[]

#default onwer login
owner_username='admin'
owner_password='1234'
while True:
    print('=====Login=====')
    print('1.owner')
    print('2.customer')
    print('3.Exsting')
    ch=int(input('choose one option:'))
    #owner login
    if ch==1:
        username=input('enter username:')
        password=input('enter password:')
        if username==owner_username and password==owner_password:
            print('login successful!')
            print('welcome owner')
            while True:
                print('====owner menu====')
                print('1.add item')
                print('2.view item')
                print('3.modify item')
                print('4.delete item')
                print('5.reports')
                print('6.logout')
                ch=int(input('choose one option:'))
                #add item
                if ch==1:
                    while True:
                        name=input('enter adding item name:')
                        price=int(input('enter price of adding item:'))
                        qty=float(input('enter quantity of adding item:'))
                        items.append(name)
                        prices.append(price)
                        quantitys.append(qty)
                        print('Item is added successfully!')
                        ch=input('do you want to add another item(yes/no):')
                        if ch=='no':
                            break
                #view item list
                elif ch==2:
                    print('Item List:')
                    for i in range(1,len(items)):
                        print(items[i],'  ',prices[i],'  ',quantitys[i])
                #modification of item
                elif ch==3:
                    while True:
                        name=input('enter modifying item name:')
                        if name in items:
                            idx=items.index(name)
                            prices[idx]=int(input('enter new price:'))
                            quantitys[idx]=float(input('enter new quantity:'))
                            print('modified successfully')
                        else:
                            print('Item not found')
                        ch=input('do you want to modify another item(yes/no):')
                        if ch=='no':
                            break
                #deleting a item
                elif ch==4:
                    while True:
                        name=input('enter deleting item name:')
                        if name in items:
                            idx=items.index(name)
                            items.pop(idx)
                            prices.pop(idx)
                            quantitys.pop(idx)
                            print('item is deleted successfully')
                        else:
                            print('item is not found')
                        ch=input('do you want to delete another item(yes/no):')
                        if ch=='no':
                            break
                #Reports
                elif ch==5:
                    while True:
                        print('----Report Menu----')
                        print('1.Total sales report')
                        print('2.Total profit report')
                        print('3.itemized profit/loss report')
                        print('4.Remaining stock report')
                        print('5.exit')
                        ch=int(input('choose one option:'))
                        #Total sales report
                        if ch==1:
                            
                            total_sales=0
                    
                            for i in range(len(cart_item)):
                                total_sales=total_sales+cart_amount[i]
                            print('Total sales:',total_sales)
                        #Total profit report
                        elif ch==2:
                            total_profit=0
                            for i in range(len(cart_item)):
                                item_name=cart_item[i]
                                qty=cart_qty[i]
                                idx=items.index(item_name)
                                profit=(prices[idx]-cost_prices[idx])*qty
                                total_profit=total_profit+profit
                            print('Total profit:',total_profit)
                        #Itemizied profit/loss report
                        elif ch==3:
                            print('---Itemizied profit/loss---')
                            print('Item,'      ',profit/loss')
                            for i in range(len(items)):
                                sold=0
                                for j in range(len(cart_item)):
                                    if items[i]==cart_items[j]:
                                        sold=sold+cart_qty[j]
                                profit=(prices[i]-cost_prices[i])*sold
                                print(items[i],'       ',profit)
                        #remaining stock
                        elif ch==4:
                            print('--Remaining stock--')
                            print('Item,'        ',left qty')
                            for i in range(len(items)):
                                print(items[i],'     ',quantitys[i])
                        elif ch==5:
                            break
                        else:
                            print('choose correct option')
                                   
                #logout
                elif ch==6:
                    print('Logging out....')
                    break
                else:
                    print('choose correct option')
        else:
            print('wrong username and password')
    #customer part
    elif ch==2:
        print('welcome customer')
        while True:
            print('-----customer menu-----')
            print('1.view items')
            print('2.add items')
            print('3.Generate bill')
            print('4.exit')
            ch=int(input('choose one option:'))
            #view items
            if ch==1:
                print('---Avaliable Items---')
                for i in range(len(items)):
                    print(items[i],'  ',prices[i])
            #adding items
            elif ch==2:

                    while True:
                        item=input('what do you want:')
                        if item=='  ' or item=='done':
                            break
                        if item in items:
                            qty=float(input('how many kgs do you want:'))
                            idx=items.index(item)
                            if qty<=quantitys[idx]:
                                amt=qty*prices[idx]
                                cart_item.append(item)
                                cart_qty.append(qty)
                                cart_amount.append(amt)
                                quantitys[idx]=quantitys[idx]-qty
                            else:
                                print('out of stock')
                        else:
                            print(item,'is not avaliable')
            #generating bill
            elif ch==3:
                print('*'*18,'vcube bill','*'*18)
                total=0
                for item in zip(cart_item,cart_qty,cart_amount):
                        print(f'{item[0]:<15}{item[1]:<15}{item[2]:<15}')
                        total=total+item[2]
                print('-'*40)
                print(' '*25,'Total Bill:',total)
            #exit
            elif ch==4:
                 print('Thank You! Visit Again...')
                 break
            else:
                print('choose correct option')
    #exit
    elif ch==3:
        ch=input('do you want to close the shop(yes/no):')
        if ch=='yes':
              print('closing the shop')
        print('exsting..')
        break
       
    else:
        print('choose the correct option')

