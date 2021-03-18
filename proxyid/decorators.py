from functools import wraps
from uuid import UUID

from .encoding import encode


def proxify(func):
    @wraps(func)
    def with_proxy(*args):
        model_instance = args[0]
        pk = model_instance.pk
        if isinstance(pk, (int, UUID)):
            return encode(pk)
    return with_proxy
