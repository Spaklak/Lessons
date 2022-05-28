'''
полиморфизм - разное поведение одного и того же метода для разных классов 
'''

"""class Person:
    age = 1
    def __add__(self,value):
        self.age += 1
        return self.age - пример полиморфизма
"""

class room:
    def __init__(self, x ,y):
        self.x = x 
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, room):
            return self.area + room_obj.area
        raise TypeError('Wrong object')

    def __eq__(self, room_obj):
        if self.area == room_obj.area:
            return True
        else:
            return False

r1 = room(3,5)
r2 = room(4,7)