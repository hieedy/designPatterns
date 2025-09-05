from threading import Thread, Lock
from time import sleep

class Singleton(type):

    _instaces = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instaces: #double check locking
            with cls._lock:
                if cls not in cls._instaces:
                    sleep(2)
                    cls._instaces[cls] = super().__call__(*args, **kwargs)
            return cls._instaces[cls]


class Product(metaclass=Singleton):

    def __init__(self):
        self.name = 'ABC'

    def print_details(self):
        print(self)


def client_code():
    p = Product()
    p.print_details()


if __name__ == '__main__':

    p1 = Thread(target=client_code)
    p2 = Thread(target=client_code)
    p1.start()
    p2.start()


