"""
Tests proxyid.encoding module
"""

import uuid
import random

import pytest
from model_bakery import baker

from proxyid.encoding import decode, encode
from proxyid.exceptions import UnkownProxiedValueError


def test_unkown_hashed_id_should_fail() -> None:
    """Tests exception in case of unkown id given"""
    with pytest.raises(UnkownProxiedValueError):
        unkown_proxied_id = "boomshakalakaB57R8g9MvnqVaL"
        decoded = decode(unkown_proxied_id)


@pytest.mark.parametrize("n", [1000])
def test_encode_decode_int(n: int) -> None:
    """Tests random int encoding for n times"""
    for seq in range(1, n+1):
        x = random.randint(1, 1000000)
        encoded = encode(x)
        decoded = decode(encoded)
        assert x == decoded


@pytest.mark.parametrize("n", [1000])
def test_encode_decode_uuid_should_succeed(n: int) -> None:
    """Tests andom uuid encoding for n times"""
    for seq in range(1, n+1):
        x = uuid.uuid4()
        encoded = encode(x)
        decoded = decode(encoded)
        assert x == decoded


@pytest.mark.parametrize("quantity", [1000])
@pytest.mark.django_db
def test_decoding_int_from_models_should_succeed(quantity: int) -> None:
    """Tests decoding int pks from n models"""
    persons = baker.make("appmock.PersonIntegerPK", _quantity=quantity)
    for person in persons:
        assert person.pk == decode(person.id_)


@pytest.mark.parametrize("quantity", [1000])
@pytest.mark.django_db
def test_decoding_uuid_from_models_should_succeed(quantity: int) -> None:
    """Tests decoding uuid pks from n models"""
    persons = baker.make("appmock.PersonUUIDPK", _quantity=quantity)
    for person in persons:
        assert person.pk == decode(person.id_)


def test_encode_with_wrong_type_argument_should_fail() -> None:
    """Tests encode with wrong type argument"""
    with pytest.raises(ValueError):
        x = "some random string"
        encode(x)


def test_decode_with_wrong_type_argument_should_fail() -> None:
    """Tests decode with wrong type argument"""
    with pytest.raises(ValueError):
        x = random.randint(1, 100)
        decode(x)
