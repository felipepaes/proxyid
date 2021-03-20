"""
Tests all views from appmock.views.py
"""

import pytest

from django.shortcuts import reverse
from appmock import models


def test_home_view_should_succeed(client) -> None:
    """Tests main index page (home) view"""
    url = reverse("home")
    res = client.get(url)
    assert res.status_code == 200


# ------------ Function Based Views ---------------


@pytest.mark.django_db
def test_function_person_list_view_should_succeed(client, mock_data) -> None:
    """Tests function based person list view"""
    url = reverse("function-person-list")
    res = client.get(url)
    assert res.status_code == 200


@pytest.mark.django_db
def test_function_person_int_detail_view_should_succeed(client, mock_data) -> None:
    """Tests person detail with integer pk function based view"""
    person = models.PersonIntegerPK.objects.all().first()
    url = reverse("function-person-int-detail", kwargs={'pk': person.id_})
    res = client.get(url)
    assert res.status_code == 200


@pytest.mark.django_db
def test_function_person_uuid_detail_view_should_succeed(client, mock_data) -> None:
    """Tests person detail with uuid pk function based view"""
    person = models.PersonUUIDPK.objects.all().first()
    url = reverse("function-person-uuid-detail", kwargs={'pk': person.id_})
    res = client.get(url)
    assert res.status_code == 200


# -------------- Class Based Views ---------------


@pytest.mark.django_db
def test_cbv_person_list_view_should_succeed(client, mock_data) -> None:
    """Tests cbv based person list view"""
    url = reverse("class-person-list")
    res = client.get(url)
    assert res.status_code == 200


@pytest.mark.django_db
def test_cbv_person_int_detail_view_should_succeed(client, mock_data) -> None:
    """Tests person detail with integer pk cbv based view"""
    person = models.PersonIntegerPK.objects.all().first()
    url = reverse("class-person-int-detail", kwargs={'pk': person.id_})
    res = client.get(url)
    assert res.status_code == 200


@pytest.mark.django_db
def test_cbv_person_uuid_detail_view_should_succeed(client, mock_data) -> None:
    """Tests person detail with uuid pk cbv based view"""
    person = models.PersonUUIDPK.objects.all().first()
    url = reverse("function-person-uuid-detail", kwargs={'pk': person.id_})
    res = client.get(url)
    assert res.status_code == 200
