"""
Tests proxyid.mixins module
"""

import pytest
from model_bakery import baker

from django.shortcuts import reverse

from proxyid.encoding import decode


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


@pytest.mark.parametrize("quantity", [20])
@pytest.mark.django_db
def test_cbv_proxyidmixin_custom_url_arg_should_succeed(quantity: int, client) -> None:
    """Tests if CBVs using ProxydMixin can use custom url arg"""

    int_persons = baker.make("appmock.PersonIntegerPK", _quantity=quantity)
    uuid_persons = baker.make("appmock.PersonUUIDPK", _quantity=quantity)

    custom_url_kwarg = "boomshakalaka"

    for person in int_persons:
        url = reverse("custom-person-int-detail",
                      kwargs={custom_url_kwarg: person.id_})
        res = client.get(url)
        assert decode(person.id_) == res.context["person"].pk

    for person in uuid_persons:
        url = reverse("custom-person-uuid-detail",
                      kwargs={custom_url_kwarg: person.id_})
        res = client.get(url)
        assert decode(person.id_) == res.context["person"].pk
