class Person:
    name = 'Ivan' # name - атрибут

    def hello(): # Hello - функция
        print("Hello world")

"""
Состаяние объекта находится через __dict__ и точку
getattr() - получение значения атрибута
setattr() - установление нового значения атрибута либо изменяет
delattr() - удаление атрибута
Person.name - обращение к атрибуту (у меня это Иван)
name - это и есть атрибут или свойство
"""
Person.age = 16
print(getattr(Person, 'age'))
setattr(Person, 'dob', '21.02.2005')
print(getattr(Person, 'dob'))
delattr(Person, 'dob')
setattr(Person, 'age', '18')
print(Person.__dict__)
Person.hello()