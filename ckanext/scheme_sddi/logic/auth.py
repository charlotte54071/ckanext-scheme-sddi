import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def scheme_sddi_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "scheme_sddi_get_sum": scheme_sddi_get_sum,
    }
