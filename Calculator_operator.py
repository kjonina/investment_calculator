
"""
Quick and simple investment calculator
Using compound interest

"""

class Calculator(object): 
    interest_rate = 0
    deposit_amount = 0
    balance = 0
    year = 0
    

#which adds interest to the balance  
    def add_interest_yearly(self):
        self.deposit_amount = eval(input('How much would you like to invest per year? '))
        self.interest_rate = eval(input('What is the compound interest rate? ___% '))
        self.year = eval(input('How many years are you planning to invest? '))
        for i in range (self.year):
            self.deposit_amount += int(self.deposit_amount * (self.interest_rate/100))
        print('Your investment has grown to',self.deposit_amount)
        
    def add_interest_monthly(self):
        self.deposit_amount = eval(input('How much would you like to invest per month? ')) * 12
        self.interest_rate = eval(input('What is the compound interest rate? ___% '))
        self.year = eval(input('How many years are you planning to invest? '))
        for i in range (self.year):
            self.deposit_amount += int(self.deposit_amount * (self.interest_rate/100))
        print('Your investment has grown to',self.deposit_amount)
        
    def operator_menu(self):
         print('1 to invest annually')
         print('2 to invest monthly')
    
    def process_operation(self):
        Calculator().operator_menu()
        func = input('Choose an operation. Here is a menu: ')
#        if func not in ['1', '2']:
#            print('Please try again')
#            items = map(float, input('Please write 1 or 2'))
        
        if func in ['1']:
            Calculator().add_interest_yearly()
        if func in ['2']:
            Calculator().add_interest_monthly()         
        
    def process(self):
        ask_again = ''
        while ask_again != 'y':
            Calculator().process_operation()
            ask_again = input('Would you like to exit the calculator (y/n)? ')

if __name__ == '__main__':
    Calculator().process()
    



        