"""
Tests proxyid.mixins module
"""

import pytest
from model_bakery import baker

from django.shortcuts import reverse

from proxyid import encode
from proxyid import decode


@pytest.mark.django_db
def test_cbv_get_object_with_mixin_should_succeed(client, mock_data):
    encoded_pk = encode(1)
    url = reverse("class-person-int-detail", kwargs={"pk": encoded_pk})
    res = client.get(url)
    print('-------------- CONTEXT[PERSON]: ', res.context["person"])
    assert res.context["person"].id_ == encoded_pk


@pytest.mark.parametrize("quantity", [20])
@pytest.mark.django_db
def test_cbv_proxyidmixin_should_succeed(quantity: int, client) -> None:
    """Tests if CBVs using ProxydMixin can retrieve objects correctly"""

    int_persons = baker.make("appmock.PersonIntegerPK", _quantity=quantity)
    uuid_persons = baker.make("appmock.PersonUUIDPK", _quantity=quantity)

    for person in int_persons:
        url = reverse("class-person-int-detail", kwargs={"pk": person.id_})
        res = client.get(url)
        assert decode(person.id_) == res.context["person"].pk

    for person in uuid_persons:
        url = reverse("class-person-uuid-detail", kwargs={"pk": person.id_})
        res = client.get(url)
        assert decode(person.id_) == res.context["person"].pk
