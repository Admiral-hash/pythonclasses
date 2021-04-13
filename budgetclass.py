class Budget:
    def __init__(self,amount):
        self.amount = amount
        self.food = 0.4 * self.amount
        self.clothing = 0.3 * self.amount
        self.entertainment = 0.3 * self.amount
    def Deposit(self):
        deposit_amount=int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT:\n"))
        new_amount = self.amount + deposit_amount
        self.food = 0.4 * new_amount
        self.clothing = 0.3 * new_amount
        self.entertainment = 0.3 * new_amount
        print('YOU DEPOSITED %d' %deposit_amount)
        print(f'YOUR NEW BUDGET DISTRIBUTION IS FOOD:{self.food},CLOTHING:{self.clothing},ENTERTAINMENT:{self.entertainment}')
    def Withdrawal(self):
        print('WITHDRAWAL')
        print('1. FOOD')
        print('2. CLOTHING')
        print('3. ENTERTAINMENT')
        option = int(input('PLEASE SELECT AN OPTION:\n'))
        if option==1:
            withdraw_food=int(input('HOW MUCH DO YOU WANT TO WITHDRAW FROM YOUR FOOD BUDGET:\n'))
            if withdraw_food<= self.food:
                print('PLEASE TAKE YOUR CASH')
            else:
                print('INSUFFICIENT FUNDS')
        elif option==2:
            withdraw_clothing=int(input('HOW MUCH DO YOU WANT TO WITHDRAW FROM YOUR CLOTHING BUDGET:\n'))
            if withdraw_clothing<= self.clothing:
                print('PLEASE TAKE YOUR CASH')
            else:
                print('INSUFFICIENT FUNDS')
        elif option==3:
            withdraw_ent=int(input('HOW MUCH DO YOU WANT TO WITHDRAW FROM YOUR ENTERTAINMENT BUDGET:\n'))
            if withdraw_ent<= self.entertainment:
                print('PLEASE TAKE YOUR CASH')
            else:
                print('INSUFFICIENT FUNDS')
        else:
            print('UNKNOWN OPTION SELECTED')
    def Transfer(self):
        print('TRANSFERS')
        print('1. FOOD')
        print('2. CLOTHING')
        print('3. ENTERTAINMENT') 
        selected_option=int(input('SELECT WHERE YOU WANT TO TRANSFER FROM:\n'))
        if selected_option==1:
            trans_amount=int(input('HOW MUCH DO YOU WANT TO TRANSFER:\n'))
            if trans_amount<=self.food:
                print('1. CLOTHING')
                print('2. ENTERTAINMENT')
                select=int(input('SELECT DESTINATION:\n'))
                if select==1:
                    self.clothing=self.clothing + trans_amount
                    print(f'YOUR NEW CLOTHING BUDGET IS:{self.clothing}')
                elif select==2:
                    self.entertainment= self.entertainment + trans_amount
                    print(f'YOUR NEW ENTERTAINMENT BUDGET IS:{self.entertainment}')
                else:
                    print('UNKNOWN OPTION SELECTED')
            else:
                print('INSUFFICIENT FUND')
        elif selected_option==2:
            trans_amount=int(input('HOW MUCH DO YOU WANT TO TRANSFER:\n'))
            if trans_amount<=self.clothing:
                print('1. FOOD')
                print('2. ENTERTAINMENT')
                select=int(input('SELECT DESTINATION:\n'))
                if select==1:
                    self.food = self.food + trans_amount
                    print(f'YOUR NEW FOOD BUDGET IS:{self.food}')
                elif select==2:
                    self.entertainment=self.entertainment + trans_amount
                    print(f'YOUR NEW ENTERTAINMENT BUDGET IS:{self.entertainment}')
                else:
                    print('UNKNOWN OPTION SELECTED')
            else:
                print('INSUFFICIENT FUND')
        elif selected_option==3:
            trans_amount=int(input('HOW MUCH DO YOU WANT TO TRANSFER:\n'))
            if trans_amount<=self.entertainment:
                print('1. FOOD')
                print('2. CLOTHING')
                select=int(input('SELECT DESTINATION:\n'))
                if select==1:
                    self.food=self.food + trans_amount
                    print(f'YOUR NEW FOOD BUDGET IS:{self.food}')
                elif select==2:
                    self.clothing= self.clothing + trans_amount
                    print(f'YOUR NEW CLOTHING IS:{self.clothing}')
                else:
                    print('UNKNOWN OPTION SELECTED')
            else:
                print('INSUFFICIENT FUND')
        else:
            print('UNKNOWN OPTION SELECTED')
    def Balance(self):
        print('CHECK BALANCE')
        print('1. FOOD')
        print('2. CLOTHING')
        print('3. ENTERTAINMENT')
        option=int(input('SELECT THE CATEGORY YOU WANT TO CHECK:\n'))
        if option==1:
            return self.food
        elif option==2:
            return self.clothing
        elif option==3:
            return self.entertainment
        else:
            print('UNKNOWN OPTION')



            
            
     
category_1= Budget(50000)
category_2= Budget(3000)
category_3= Budget(2500)
category_4= Budget(100000)
print(category_1.Deposit())
print(category_2.Withdrawal())
print(category_3.Transfer())
print(category_4.Balance())