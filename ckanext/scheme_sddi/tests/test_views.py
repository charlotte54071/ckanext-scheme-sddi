"""Tests for views.py."""

import pytest

import ckanext.scheme_sddi.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "scheme_sddi")
@pytest.mark.usefixtures("with_plugins")
def test_scheme_sddi_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("scheme_sddi.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, scheme_sddi!"
