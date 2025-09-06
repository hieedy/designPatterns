# Overcme propblem of Enforcing immutability on class Method 1
# As we dont have concept of private variables in python so any object can change it anywhere so
# overriding the __setattr__() to control the setting of value.

# Problems:
# More prone to errors, less readability. a big constructor, v
# Again if we want to add validations it will increase code for constructor.
class DBConfig:
    def __init__(self, db_type: str, host: str, port: str,
                username: str, password: str, ssl: bool = True,
                timeout: int = 30, pool_size: int = 5):
        super().__setattr__(name='db_type', value=db_type)
        super().__setattr__(name='host', value=host)
        super().__setattr__(name='port', value=port)
        super().__setattr__(name='username', value=username)
        super().__setattr__(name='password', value=password)
        super().__setattr__(name='ssl', value=ssl)
        super().__setattr__(name='timeout', value=timeout)
        super().__setattr__(name='pool_size', value=pool_size)
        super().__setattr__(name='_frozen', value=True)

    #enforcing no
    def __setattr__(self, key, value):
        if self.__getattribute__(self, '_frozen', False):
            raise AttributeError(f'Class {self.__class__.name} is immutable')
        super().__setattr__(name=key, value=value)

    def create_connection(self):
        pass

    def close_connection(self):
        pass

    def get_data(self):
        pass

    # other methods
