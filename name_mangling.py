'''
искажение имён (перед переменной, к примеру name, если дописать __, то как раз и получиться name mangling)
к примеру:
class Account:
    def __init__(self,balance):
        self.__balance = balance

a = Account(0)
Тут нельзя будет увеличить наш balance, даже если мы к нему обратимся через a.__balance
Сам питон делает подмену на _Account__balance
__balance == _Account__balance, поэтому питон не ломается 
'''
white = '\033[00m'
green = '\033[0;92m' 
red = '\033[1;31m'


class Account:
    def __init__(self,name, balance):
        self.name = name
        self.__balance = balance
        self.history = [] 

    def deposit(self, amount): 
        self.__balance += amount
        self.show_balance()
        self.history.append(amount)
    
    def spent(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} rubles')
            self.show_balance()
            self.history.append(-amount)
        else:
            print('Not enough money')
            self.show_balance()
    
    def show_balance(self): 
        print(f'Balance: {self.__balance} rubles')
    
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