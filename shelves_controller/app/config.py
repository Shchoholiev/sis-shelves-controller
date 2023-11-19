import json
import os

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

    current_directory = os.path.dirname(os.path.realpath(__file__))

    appconfig_file_path = os.path.join(current_directory, 'appconfig.json')
    app_config = read_json_file(appconfig_file_path)

    deviceconfig_file_path = os.path.join(current_directory, 'deviceconfig.json')
    device_config = read_json_file(deviceconfig_file_path)

    return {**app_config, **device_config}

config = load_config()