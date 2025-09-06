#Here the ide is same as methohd 2
# it's just we can use @propety and @<protery_nme>.setattr in python so just pythonic way
# But here chaining wont happen as in the setter you are not returning self.
# Still possible to chain if you want (by making setters return self,
# but that breaks the usual property semantics, so most Python devs avoid chaining with properties).
from dataclasses import dataclass

@dataclass(frozen=True)
class DBConfig:
    db_type: str
    host: str
    port: int
    username: str
    password: str
    ssl: bool = False
    timeout: int = 30
    pool_size: int = 5


class DBConfigBuilder:
    def __init__(self):
        self._db_type = None
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._ssl = False
        self._timeout = 30
        self._pool_size = 5

    # ---- properties with validation ----
    @property
    def db_type(self):
        return self._db_type

    @db_type.setter
    def db_type(self, value):
        self._db_type = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if not (0 < value < 65536):
            raise ValueError("Port must be 1-65535")
        self._port = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def ssl(self):
        return self._ssl

    @ssl.setter
    def ssl(self, value: bool):
        self._ssl = bool(value)

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        if value < 1:
            raise ValueError("Timeout must be > 0")
        self._timeout = value

    @property
    def pool_size(self):
        return self._pool_size

    @pool_size.setter
    def pool_size(self, value):
        if value < 1:
            raise ValueError("Pool size must be > 0")
        self._pool_size = value

    # ---- final build ----
    def build(self):
        if not all([self._db_type, self._host, self._port, self._username, self._password]):
            raise ValueError("Missing required DB config fields")
        return DBConfig(
            db_type=self._db_type,
            host=self._host,
            port=self._port,
            username=self._username,
            password=self._password,
            ssl=self._ssl,
            timeout=self._timeout,
            pool_size=self._pool_size
        )
