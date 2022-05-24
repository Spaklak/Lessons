'''
local 
enclosed
global
builtins
'''

# name = 'Egor'
class Person:
    name = 'Dima'

    @classmethod # чтобы в классе через метод можно было поменять 'Dima' на что-либо другое. Иначе мы сможем только читать переменную через self.name (cls тут для красоты)
    def change_name(cls, name):
        cls.name = name

p = Person()
print(p.__dict__)
p.change_name('asdsdada')

print(p.__dict__)
print(Person.name)