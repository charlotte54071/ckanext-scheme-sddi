"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.scheme_sddi.logic import validators


def test_scheme_sddi_reauired_with_valid_value():
    assert validators.scheme_sddi_required("value") == "value"


def test_scheme_sddi_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.scheme_sddi_required(None)
