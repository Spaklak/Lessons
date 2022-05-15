class Person:
    name = 'Ivan'
print(Person.name) #возвращает имя
print(Person.__name__) #имя класса
print(dir(Person)) # доступные атрибуды 
print(Person.__class__) #тип класса
p = Person()
print(p.__class__) # тип объекта
