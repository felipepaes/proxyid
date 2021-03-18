"""
Tests django fixtures mock data, check appmock/fixtures/person.json
"""

import pytest

from appmock import models


@pytest.mark.django_db
def test_load_fixtures_should_succeed(mock_data) -> None:
    """Tests if mock data fixtures loads"""
    int_persons = models.PersonIntegerPK.objects.all()
    uuid_persons = models.PersonUUIDPK.objects.all()
    assert len(int_persons) > 0
    assert len(uuid_persons) > 0
