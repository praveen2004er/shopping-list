import json

def read_config(config_file_path):
    with open(config_file_path, 'r') as file:
        data = json.load(file)
    return data