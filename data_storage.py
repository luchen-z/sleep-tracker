import json
import os
import pprint

from utils import sort_nested_dict

SLEEP_DATA_DIRECTORY = 'data_store/sleep_data'
CONFIG_FILE = 'data_store/user_config.json'


# Function to save user records to separate JSON files
def save_to_json_file(users_records):
    directory = SLEEP_DATA_DIRECTORY
    if not os.path.exists(directory):
        os.makedirs(directory)

    users_records = sort_nested_dict(users_records)

    for user, records in users_records.items():
        filename = os.path.join(directory, f"{user}.json")
        with open(filename, 'w') as f:
            json.dump(records, f, indent=4)
    return users_records


# Function to read all user JSON files and combine them into a single dictionary
def read_json_file():
    directory = SLEEP_DATA_DIRECTORY
    if not os.path.exists(directory):
        os.makedirs(directory)

    all_data = {}

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            user = filename[:-5]  # Remove the .json extension to get the user name
            filepath = os.path.join(directory, filename)
            with open(filepath) as fp:
                data_loaded = json.load(fp)
                all_data[user] = sort_nested_dict(data_loaded)

    pprint.pp(all_data)
    return all_data


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
