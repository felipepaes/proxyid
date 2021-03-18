"""
Tests proxyid.encoding module
"""

import uuid
import random

import pytest

from proxyid import decode, encode
from proxyid.exceptions import UnkownProxiedValueError


@pytest.mark.parametrize("n", [100])
def test_encode_decode_int(n: int) -> None:
    """Tests random int encoding for n times"""
    for seq in range(1, n+1):
        x = random.randint(1, 1000000)
        encoded = encode(x)
        decoded = decode(encoded)
        assert x == decoded


@pytest.mark.parametrize("n", [100])
def test_encode_decode_uuid_should_succeed(n: int) -> None:
    """Tests andom uuid encoding for n times"""
    for seq in range(1, n+1):
        x = uuid.uuid4()
        encoded = encode(x)
        decoded = decode(encoded)
        assert x == decoded


def test_unkown_hashed_id_should_fail() -> None:
    """Tests exception in case of unkown id given"""
    with pytest.raises(UnkownProxiedValueError):
        unkown_proxied_id = "boomshakalakaB57R8g9MvnqVaL"
        decoded = decode(unkown_proxied_id)
