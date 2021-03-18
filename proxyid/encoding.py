import uuid
from typing import Union

from .exceptions import UnkownProxiedValueError
from .utils import make_hashid


hash = make_hashid()


def encode(x: Union[int, uuid.UUID]) -> str:
    if isinstance(x, int):
        return hash.encode(x)
    elif isinstance(x, uuid.UUID):
        return hash.encode_hex(x.hex)
    else:
        raise ValueError(
            f"Expected argument of type int or UUID but received a {type(x)}")


def decode(x: str) -> Union[int, uuid.UUID]:
    if isinstance(x, str):
        decoded = hash.decode(x)
        if len(decoded) == 1:
            return decoded[0]
        elif len(decoded) > 1:
            return uuid.UUID(hash.decode_hex(x))
        else:
            raise UnkownProxiedValueError(x)
    else:
        raise ValueError(
            f"Expected argument of type str but received a {type(x)}")
