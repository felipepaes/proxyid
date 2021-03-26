import uuid
from typing import Union

from .exceptions import UnkownProxiedValueError
from .utils.factory import make_hash


hash = make_hash()


def encode(x: Union[int, uuid.UUID]) -> str:
    """Encode int or uuid pk to str"""
    if isinstance(x, int):
        return hash.encode(x)
    elif isinstance(x, uuid.UUID):
        return hash.encode_hex(x.hex)
    else:
        raise ValueError(
            f"Expected argument of type int or UUID but received a {type(x)}")


def decode(x: str) -> Union[int, uuid.UUID]:
    """
    Decode a proxied value (str) back to it's original value (int or uuid)

    If the len of decoded is equal to 1, it assumes the original value
    was an int, if greater then 1, it was originally an hex, otherwise
    it's  an unkown value which is wrong or was hashed with a different
    configuration.
    """
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
