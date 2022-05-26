class Soda:
    def __init__(self, ingredient=None):
        if ingredient != None:
            self.ingredient = ingredient
        else:
            self.ingredient = None
        
    def show_my_drink(self):
        if self.ingredient != None:
            print(f'Газировка {self.ingredient}')
        else:
            print('Обчная газировка')
        
        