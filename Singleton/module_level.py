class Singleton:
    def __init__(self):
        self.a = 5
        self.b = 40

    def add(self):
        return self.a + self.b


singleton = Singleton()
# No just import this object wherever need.
# But still it dees not enforce anthing anyone can create a new object by importing the class simply.

