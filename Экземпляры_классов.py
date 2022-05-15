class Person:
    name = 'Ivan'

print(Person.__dict__)

p1 = Person() # создание экземляра класса
p2 = Person()
p1.age = 123 # добавляем элемент экземляру, но обратиться к нему нельяз
'''print(p1.__dict__)
print(p1.name)'''
print(p1.age) # видимо можно
Person.name = 'Egor'
print(p1.name) # если что-то менять в классе, то в экземпляре тоже это меняет