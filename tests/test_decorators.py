"""
Tests proxyid.decorators module
"""

import pytest

from proxyid.encoding import decode

from appmock import models


@pytest.mark.django_db
def test_proxify_decorator_intpk_should_succeed(mock_data) -> None:
    """Tests if the proxify decorator is exposing the proxied int pk"""
    int_persons = models.PersonIntegerPK.objects.all()
    assert len(int_persons) > 0
    for person in int_persons:
        assert person.pk == decode(person.id_)


@pytest.mark.django_db
def test_proxify_decorator_uuidpk_should_succeed(mock_data) -> None:
    """Tests if the proxify decorator is exposing the proxied uuid pk"""
    uuid_persons = models.PersonUUIDPK.objects.all()
    assert len(uuid_persons) > 0
    for person in uuid_persons:
        assert person.pk == decode(person.id_)
