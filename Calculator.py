
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
        
    def deposit(self):
        self.deposit_amount = eval(input('How much would you like to invest? '))

#which adds interest to the balance  
    def add_interest(self):
        self.interest_rate = eval(input('What is the compound interest rate? ___% '))
        self.year = eval(input('How many years are you planning to invest? '))
        for i in range (self.year):
            self.balance += int(self.balance * (self.interest_rate/100))
        print('Your investment has grown to',self.balance)
        
        
first = Calculator(3000)


first.add_interest()



        