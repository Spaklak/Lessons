
class Person:
    def hello(self):
        print('Hello')
    @staticmethod #чтобы метод был статичным (без тербований доступа к экземплярам класса), экономит память пк. Но независимы
    def gooodby():
        print('GoodBye')


a = Person()
b = Person()
""" 
p = Person()
p.gooodby() # не сработает без staticmethod
"""
''' id у статичных методов будут одинаковыми 
 __dict__ тоже будут одинаковыми
'''