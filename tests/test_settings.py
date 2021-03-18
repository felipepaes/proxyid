"""
Tests proxyid configuration in django's settings.py
"""
import pytest

from proxyid.exceptions import ProxyidConfigurationError

from proxyid.utils import make_hashid


def test_missing_config_should_fail(settings) -> None:
    """Tests proxyid settings is missing"""
    with pytest.raises(ProxyidConfigurationError):
        settings.PROXYID = None
        hash = make_hashid()


def test_missing_salt_should_fail(settings) -> None:
    """Tests proxyid settings min_length configuration is missing"""
    with pytest.raises(ProxyidConfigurationError):
        settings.PROXYID = {"min_length": 25}
        hash = make_hashid()


def test_missing_min_length_should_fail(settings) -> None:
    """Tests proxyid settings salt configuration is missing"""
    with pytest.raises(ProxyidConfigurationError):
        settings.PROXYID = {"salt": "A grain of salt"}
        hash = make_hashid()
