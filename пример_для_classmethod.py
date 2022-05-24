class Person:
    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def from_file(cls,path):
        with open(path) as f:
            name = f.read().strip() # strip - удаление пробелов в начале и конце и других элементов, которые указаны в нём 
        return cls(name = name)

    @classmethod
    def from_obj(cls,obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name = name)
        return cls