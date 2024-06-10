import pprint

from data_storage import save_to_json, read_json_file
from user_interface import get_sleep_info, get_user_info, has_sleep_info_to_record, summarize_sleep


def main():
    users_records = read_json_file()
    user_name = get_user_info()

    while has_sleep_info_to_record() == "Y":
        sleep_info = get_sleep_info()
        save_sleep_info(sleep_info, user_name, users_records)
        pprint.pp(users_records)

    save_to_json(users_records)
    print("Thank you.")
    exit()


def save_sleep_info(sleep_info, user_name, users_records):
    # Save the sleep record(s) in to data structure
    sleep_records = sleep_info[0]
    quality_recorded = sleep_info[1]
    for record in sleep_records:
        summarize_sleep(users_records, user_name, record[0], record[1], quality_recorded)


if __name__ == '__main__':
    main()

