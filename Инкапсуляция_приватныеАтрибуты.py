
"""
Инкапсуляция - создание объекта, который содержит в себе данные методы для работы с данными (наружного объекта)
Публичный интерфейс - набор свойств и методов, которые будут использоваться другими объектами
Велик: руль, педаль и тормоза (публично), а не публично - цепи, подшипники, спицы и так далее 
ПК: клавиатура, дисплей, мышь; видюха, проц и так далее 
Упаковка того, что пользователю не надо видеть и называется инкапсуляцией (от англ In-Capsula)
Приватные атрибуты класса обозначаются одним нижним подчеркиванием 
"""

class Person:
    def __init__(self,name,surname):
        self._name = name # private
        self._surname = surname # private
        self.name = f'{self._name} {self._surname}'

    
p = Person('Egor', 'Kruchaev')
print(p.name)
