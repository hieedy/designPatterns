# not reusable.
class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    def __init__(self,a,b):
        self.a = 5
        self.b = 10

    def add(self):
        return self.a + self.b


singleton1 = Singleton(5, 2)
singleton2 = Singleton(3,2)

print(singleton1 is singleton2)
