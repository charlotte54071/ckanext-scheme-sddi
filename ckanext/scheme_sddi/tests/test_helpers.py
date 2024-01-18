"""Tests for helpers.py."""

import ckanext.scheme_sddi.helpers as helpers


def test_scheme_sddi_hello():
    assert helpers.scheme_sddi_hello() == "Hello, scheme_sddi!"
