'''
суть хэширования - преобразовывать строку неопред. длинны в строку опред. длинны
'''

from unicodedata import name


class Person:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person) and self.name == person_obj.name


p1 = Person('Ivan')
p2 = Person('Ivan')
print(hash(p1))
print(hash(p2))
# хеши равны => можно использовать как ключ в словаре и по обоим будет получено одно и тоже
d = {p1: 'egor'}
print(d.get(p2))