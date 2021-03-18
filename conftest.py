import pytest

from django.core.management import call_command


@pytest.fixture(scope="function")
def mock_data(django_db_setup, django_db_blocker) -> None:
    """Injects fixtures data into database during runtime"""
    with django_db_blocker.unblock():
        call_command("loaddata", "person.json")
