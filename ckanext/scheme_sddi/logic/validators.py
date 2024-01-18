import ckan.plugins.toolkit as tk


def scheme_sddi_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "scheme_sddi_required": scheme_sddi_required,
    }
