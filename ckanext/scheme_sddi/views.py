from flask import Blueprint


scheme_sddi = Blueprint(
    "scheme_sddi", __name__)


def page():
    return "Hello, scheme_sddi!"


scheme_sddi.add_url_rule(
    "/scheme_sddi/page", view_func=page)


def get_blueprints():
    return [scheme_sddi]
