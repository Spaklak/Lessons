class Person:
    def hello():
        print('hello')

p = Person() # экземпляр

print(type(p.hello)) # это метод
print(type(Person.hello)) # это функция

"""
методы - классы обёрткаи (объединяют в себе функции классов)

"""
class Person:
    def hello(self):
        print(self) # self - чтобы получить доступ к пространству имён экземпляров из самих классов 


