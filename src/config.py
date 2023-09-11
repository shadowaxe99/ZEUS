import json


def load_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config


def save_config(config, file_path):
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)
