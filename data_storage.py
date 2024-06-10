import json
import os
import pprint

FILENAME = 'data/sleep_tracker_data.json'
CONFIG_FILE = 'data/user_config.json'


def save_to_json(users_records):
    with open(FILENAME, 'w') as f:
        json.dump(users_records, f, indent=4)


def read_json_file():
    if not os.path.exists(FILENAME):
        # Ensure the directory for the file exists
        os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
        # Create an empty file
        with open(FILENAME, 'w') as file:
            json.dump({}, file)

    with open(FILENAME) as fp:
        data_loaded = json.load(fp)
    pprint.pp(data_loaded)
    return data_loaded


def read_user_name():
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, 'r') as file:
        config = json.load(file)
    return config.get('user_name', None)


def save_user_name(user_name):
    config = {"user_name": user_name}
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)
