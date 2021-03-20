from functools import wraps
from uuid import UUID

from .encoding import encode


def proxify(func):
    """Encodes the model instance primary key and exposes it as a property"""
    @wraps(func)
    def with_proxy(*args):
        model_instance = args[0]  # gets model instance from *args
        pk = model_instance.pk
        if isinstance(pk, (int, UUID)):
            return encode(pk)
    return with_proxy
