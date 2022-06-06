'''
dry - dont repeat yourself
'''

class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self, name, surname): # сюда нужно дописать также name 
        super().__init__(name)
# благодаря этой штуке (super) мы можем принимать и устанавливать name у экземпляра класса Student (берём функции у родительского класса (того, который выше)). Порядок важен
        self.surname = surname

s = Student('Egor', 'Mazeloff')
print(s.__dict__)


class Person1:
    def hello(self):
        print(f'Bound with {self}')

class Student1(Person1):
    def hello(self):
        print('Student obj.hello() is called')
        super().hello() # тут будет hello у Student, поскольку hello студента раньше 

s = Student1()