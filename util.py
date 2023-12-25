def project_dict(original_dict, keys_to_project):
    return {key: original_dict[key] for key in keys_to_project if key in original_dict}

