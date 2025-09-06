# Problems:
# very big constructor if the optional parameters list keeps on growing.
# if we want to add validation ex: passnowrd != null, timeout > 30 , etc will add alot of logic in the constructor itself.
# Violate single responsibility principlee.

# Solution -- expose getter and setter for each attribute(useful in another languages like in java/c++.etc)
# OR use @property ana @<property_name>.settattr decorator (MORE pythonic way) (if the object mutability is not the concern)

# Another problem: -- But as our problem statement says DBConfig object should
# be immutable i.e. once created should not be allowed to change.
# so exposing setter in the DBConfig class itself is not a solution.

class DBConfig:

    def __init__(self, db_type: str, host: str, port: str,
                username: str, password: str, ssl: bool = True,
                timeout: int = 30, pool_size: int = 5):
        self.db_type = db_type
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssl = ssl
        self.timeout = timeout
        self.pool_size = pool_size

    def create_connection(self):
        pass

    def close_connection(self):
        pass

    def get_data(self):
        pass

    # other methods
