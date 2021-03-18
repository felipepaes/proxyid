from django.conf import settings

from hashids import Hashids
from .exceptions import ProxyidConfigurationError


def make_hashid() -> Hashids:
    try:
        config = settings.PROXYID
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
