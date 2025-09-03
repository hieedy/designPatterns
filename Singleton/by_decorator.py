# reusable
# but now the class is function wrapped

def singleton(cls):
    _instances = {}

    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return wrapper


@singleton
class Demo:
    def __init__(self):
        self.a = 5
        self.b  = 10

    def add(self):
        return self.a + self.b


if __name__ == '__main__':
    d1 = Demo()
    d2 = Demo()
    print(d1 is d2)
