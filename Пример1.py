'''
банковский счёт
'''
white = '\033[00m'
green = '\033[0;92m' 
red = '\033[1;31m'


class Account:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        self.history = [] # информации о транзакциях

    def deposit(self, amount): #метод
        self.balance += amount
        self.show_balance()
        self.history.append(amount)
    
    def spent(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'You spent {amount} rubles')
            self.show_balance()
            self.history.append(-amount)
        else:
            print('Not enough money')
            self.show_balance()
    
    def show_balance(self): # ничего не принимает т.к. balance у нас уже принимает метод unit, поэтому ничего передавать не нужно 
        print(f'Balance: {self.balance} rubles')
    
    def show_history(self):
        for amount in self.history:
            if amount > 0:
                transaction = 'deposited'
                color = green
            else:
                transaction = 'spent'
                color = red
            print(f'{color} {amount} {white} {transaction}')

a = Account('Egor', 0)