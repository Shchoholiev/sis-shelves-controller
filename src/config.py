import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Config file not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error parsing JSON: {file_path}")
        return {}

def load_config():
    """Load configuration from appconfig.json and deviceconfig.json"""

    app_config = read_json_file('appconfig.json')
    device_config = read_json_file('deviceconfig.json')

    return {**app_config, **device_config}

config = load_config()