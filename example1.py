class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.hello = f'My name is {self.surname} {self.name}. I am {self.age}.'
    
p = Person('Egor', 'Kruchaev', 10)
print(p.hello)