"""
__slots__ - ограничивает колв-о набора свойств и методов
Пример:
"""

from ast import Attribute


class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, age, name) -> None:
        self.name = name
        if self.name != 'Николай':
            self.name = f'Я не {self.name}, а Николай'
        self.age = age

p1 = Nikola(14,'Макс')
p2 = Nikola(16,'Николай')
print(p1.name)
print(p2.name)
try:
    p1.surname = 'Лёхович'
    print(p1.surname)
except AttributeError:
    print(f'У Николая нет цели, а есть только путь')