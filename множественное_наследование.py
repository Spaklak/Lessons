"""
тот, кто левее из родителей, тот и будет вызван. То-есть в нашем примере выведется I am student
mro - множественное наследование
"""

class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I like {self.food}')


class Person:
    def hello(self):
        print('I am Person')

class Student(FoodMixin, Person):
    food = 'Pizza'
    def hello(self):
        print('I am Student')

class Prof(Person):
    def hello(self):
        print('I am Prof')

class Someomne(Student, Prof):
    pass

a=Student()
s = Someomne()
s.hello()