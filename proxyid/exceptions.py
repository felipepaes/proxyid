from typing import Union


class UnkownProxiedValueError(Exception):
    """Exception for unkown values given to be decoded"""

    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return (f"Proxied value {self.value} is unkown. "
                "The value is wrong or was hashed with a different salt.")


class ProxyidConfigurationError(Exception):
    """Exception for missing configuration"""

    def __init__(self, value: Union[str, None] = None):
        self.value = value

    def __str__(self) -> str:
        if self.value is not None:
            return (f"PROXYID[{self.value}] is missing, "
                    "check settings.py")
        else:
            return "PROXYID dict could not be found in settings.py"
