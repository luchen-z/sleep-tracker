import json
import os
import pprint

filename = 'data/sleep_tracker_data.json'


def save_to_json(users_records):
    with open(filename, 'w') as f:
        json.dump(users_records, f, indent=4)


def read_json_file():

    if not os.path.exists(filename):
        # Ensure the directory for the file exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        # Create an empty file
        with open(filename, 'w') as file:
            json.dump({}, file)

    with open(filename) as fp:
        data_loaded = json.load(fp)
    pprint.pp(data_loaded)
    return data_loaded
