# Overcme propblem of Enforcing immutability on class Method 2
# By using data class
# this will allow not to set the values after object creation.

# Now how will i create object such that i am setting values to the DBConfig ?
# create anopther helper class that will helps you to build this DBCOnfig class

from dataclasses import dataclass
from typing import Self


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

    def set_db_type(self, db_type) -> Self:
        self._db_type = db_type
        return self

    def set_host(self, host):
        self._host = host
        return self

    def set_port(self, port):
        if not (0 < port < 65536):
            raise ValueError("Port must be 1-65535")
        self._port = port
        return self

    def set_username(self, username):
        self._username = username
        return self

    def set_password(self, password):
        self._password = password
        return self

    def enable_ssl(self, enabled=True):
        self._ssl = enabled
        return self

    def set_timeout(self, timeout):
        if timeout < 1:
            raise ValueError("Timeout must be > 0")
        self._timeout = timeout
        return self

    def set_pool_size(self, pool_size):
        if pool_size < 1:
            raise ValueError("Pool size must be > 0")
        self._pool_size = pool_size
        return self

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



