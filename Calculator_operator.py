
"""
Quick and simple investment calculator
Using compound interest

"""

class Calculator(object): 
    interest_rate = 0
    deposit_amount = 0
    balance = 0
    year = 0
    
    def __init__(self, balance): 
        self.balance = balance 

#which adds interest to the balance  
    def add_interest_yearly(self):
        self.deposit_amount = eval(input('How much would you like to invest per year? '))
        self.interest_rate = eval(input('What is the compound interest rate? ___% '))
        self.year = eval(input('How many years are you planning to invest? '))
        for i in range (self.year):
            self.deposit_amount += int(self.deposit_amount * (self.interest_rate/100))
        print('Your investment has grown to',self.balance)
        
    def add_interest_monthly(self):
        self.deposit_amount = eval(input('How much would you like to invest per month? '))
        self.interest_rate = eval(input('What is the compound interest rate? ___% '))
        self.year = eval(input('How many years are you planning to invest? '))
        for i in range (self.year):
            self.deposit_amount*52 += int(self.deposit_amount * (self.interest_rate/100))
        print('Your investment has grown to',self.balance)
        
    def operator_menu(self):
         print('1 to invest annually')
         print('2 to invest monthly')
    
    def process_operation(self):
        Calculator().operator_menu()
        func = input('Choose an operation. Here is a menu: ')
        if func not in ['1', '2']:
            items = map(float, input('Please write 1 or 2'))
        
        if func in ['1']:
            print('Total of all numbers in the set is: ', Calculator().add_interest_monthly())
        if func in ['2']:
            print('Results of subtracting of all numbers in the set is: ', Calculator().add_interest_yearly())            
        
first = Calculator(3000)


first.add_interest()



        