import logging

from hashids import Hashids

from proxyid.exceptions import ProxyidConfigurationError

try:
    from django.conf import settings
except ImportError:
    logging.exception(
        "\033[91mProxyid failed to import Django settings."
        "Please, make sure Django is installed.\033[0m")


def make_hash(hash_type="hashids") -> Hashids:
    """Factory function, can make different encoders in the future if needed"""

    def make_hashid() -> Hashids:
        """Build a Hashid instance based on Django's settings.py configuration"""
        try:
            config = settings.PROXYID["hashids"]
            salt = config.get("salt", None)
            min_length = config.get("min_length", None)

            if salt is None:
                raise ProxyidConfigurationError("salt")
            elif min_length is None:
                raise ProxyidConfigurationError("min_length")
            else:
                return Hashids(salt=salt, min_length=min_length)
        except AttributeError:
            raise ProxyidConfigurationError

    if hash_type == "hashids":
        return make_hashid()
    else:
        raise ValueError(f"There is no {hash_type} hash_type")
