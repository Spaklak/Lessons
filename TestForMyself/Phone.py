white = '\033[00m'
yellow = '\033[0;33m'
green = '\033[0;92m'
class Phone:
    def __init__(self, number, model, weight) -> None:
        self.number = number
        self.model = model
        self.weight = weight

    def get(self):
        print(f' Модель: {self.model}.\n Вес: {self.weight}.\n Номер: {self.number}')

    def receiveCall(self,name):
        print(f'Звонит: {yellow}{name}{white}')
        self.get_Number()

    def get_Number(self):
        print(f'Номер: {green}{self.number}{white}')

p1 = Phone('+79843777898', 'Huawei', 101)
p2 = Phone('+79843777345', 'Xiaomi', 112)
p3 = Phone('+77777777777', 'Apple', 1000)