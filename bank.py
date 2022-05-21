
class Bank:
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance
        self.history = []

    def add(self, amount):
        self.balance += amount
        print(f'{self.name}, на Ваш счёт зачислено {amount} рублей')
        self.history.append(amount)

    def spent(self,amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'{self.name}, с Вашего счёта снято {amount} рублей')
            self.history.append(-amount)
        else:
            print(f'{self.name}, на Вашем счёте:{self.balance}. Для операции необходимо ещё {amount - self.balance} рублей')

    def show_balance(self):
        print(f'{self.name}, на Вашем счёте: {self.balance} рублей.')
        self.dolg()

    def show_history(self):
        for i in self.history:
            if i > 0:
                print(f'{self.name}, на Ваш было счёт зачислено {i} рублей ')
            else:
                print(f'{self.name}, с Вашего счёта было списано {i} рублей')
    
    def dolg(self):
        print('На вашем счёте долг 100р')

Egor = Bank('Егор Кручаев', 0)