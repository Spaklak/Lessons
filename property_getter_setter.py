"""
getter - для чтение значения 
setter - для установления нового значения  
"""

class Person:
    def __init__(self,name):
        self._name = name

    def get_name(self):
        print('Form get_name(')
        return self._name

    def set_name(self,value):
        print('From set_name()')
        self._name = value
    '''первый способ
    name = property(fget=get_name, fset=set_name) # name - атрибут класса, а property - отдельный класс в питоне, который принимает 2 значения fget(чтение) и fset(установка)
    '''
    """
    второй способ
    name = property()
    name = name.getter(get_name)
    name = name.setter(set_name)
    """
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

p = Person('Egor')
print(p.__dict__)
print(p.name)
p.name = 'ivan'
print(p.__dict__)