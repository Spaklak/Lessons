"""
class Student(Person), Perosn - это родительский класс
"""

class Intel_cpu:
    cpu_socket = 1151
    name = 'Intel'

class I7(Intel_cpu):
    pass

class I5(Intel_cpu):
    pass
#isinstance - конткретный экземпляр имеет какой-либо атрибут, который достался от родителя модель такая: экземпляр, класс от которого наследуется что-либо
i5 = I5()
i7 = I7()
print(isinstance(i5, Intel_cpu))
#issubclass - отношения между классами
print(issubclass(I7, Intel_cpu))

"""class Person:
    def hello(self):
        print('I am Person')

class Student(Person):
    def hello(self):
        print('I am student')

сначала поиск осуществляется в нашем классе, а если ничего не находится, то уходит в родительский 

s = Student()
print(s.hello())
выведет I am student
"""
class Person:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print(f'I am {self.name}')

class Student(Person):
    pass

s = Student('Egor')
print(s.hello())