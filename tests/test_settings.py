"""
Tests proxyid configuration in django's settings.py
"""
import pytest
import sys

from proxyid.exceptions import ProxyidConfigurationError

from proxyid.utils.factory import make_hash


def test_missing_config_should_fail(settings) -> None:
    """Tests proxyid settings is missing"""
    with pytest.raises(ProxyidConfigurationError):
        settings.PROXYID["hashids"] = None
        hash = make_hash()


def test_missing_salt_should_fail(settings) -> None:
    """Tests proxyid settings min_length configuration is missing"""
    with pytest.raises(ProxyidConfigurationError):
        settings.PROXYID["hashids"] = {"min_length": 25}
        hash = make_hash()


def test_missing_min_length_should_fail(settings) -> None:
    """Tests proxyid settings salt configuration is missing"""
    with pytest.raises(ProxyidConfigurationError):
        settings.PROXYID["hashids"] = {"salt": "A grain of salt"}
        hash = make_hash()
