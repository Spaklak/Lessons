"""
self.name = p.name 'ivan'
init - вызывает автоматом
"""

class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)

'''теперь можно написать p = Person('Ivan') и конструктор сам создаст p.name (сначала init использует __new__(), который и создаёт сам экземляр) 

__init__ заменяет такую штуку, как p.age = 123 (к примеру). Можно просто написать p = Person(123)


python -i ИнициализацияЭкземпляровИ__unit__Метод.py чтобы что-то запустить в консоли

'''