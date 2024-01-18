import ckan.plugins.toolkit as tk
import ckanext.scheme_sddi.logic.schema as schema


@tk.side_effect_free
def scheme_sddi_get_sum(context, data_dict):
    tk.check_access(
        "scheme_sddi_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.scheme_sddi_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'scheme_sddi_get_sum': scheme_sddi_get_sum,
    }
