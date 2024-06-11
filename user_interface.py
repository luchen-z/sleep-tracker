import pprint
from datetime import datetime, timedelta
from bisect import insort

from data_storage import read_user_name, save_user_name
from utils import sort_nested_dict


def split_record_if_overnight(sleep_time_recorded, wake_time_recorded):
    if sleep_time_recorded.date() != wake_time_recorded.date():
        intermediate_time_1 = sleep_time_recorded.replace(hour=23, minute=59)
        intermediate_time_2 = wake_time_recorded.replace(hour=0, minute=0)
        return [[sleep_time_recorded, intermediate_time_1],
                [intermediate_time_2, wake_time_recorded]]
    else:
        return [[sleep_time_recorded, wake_time_recorded]]


def get_sleep_info():
    # Input phase
    sleep_time_recorded = get_date_and_time("Sleep")
    wake_time_recorded = get_date_and_time("Wake-Up")
    quality_recorded = get_quality()

    # Split the sleep record if it is overnight
    sleep_records = split_record_if_overnight(sleep_time_recorded, wake_time_recorded)

    return [sleep_records, quality_recorded]


def get_user_info():
    user_name = read_user_name()
    print("")
    print(f"Welcome back, {user_name}!")

    new_user_name = input(f"If you are {user_name}, just press ENTER. If not, please type in your name: ").strip()
    if not new_user_name:
        return user_name
    else:
        save_user_name(new_user_name)
        return new_user_name


def get_date_and_time(prompt):
    print("")
    print("Please enter your " + str(prompt).lower() + " date and time...")
    while True:
        try:
            date = get_date_with_shortcuts(prompt)
            time = get_time(prompt)
            return datetime.combine(date, time)
        except ValueError:
            print("Invalid date or time format. Please enter the date in YYYY-MM-DD and time in HH:MM format.")


def get_date_with_shortcuts(prompt):

    today = datetime.today().date()
    shortcuts = {
        '0': today,
        '1': today - timedelta(days=1),
        '2': today - timedelta(days=2),
        '3': today - timedelta(days=3),
        '4': today - timedelta(days=4),
        '5': today - timedelta(days=5),
        '6': today - timedelta(days=6),
    }

    shortcuts_msg = "Shortcuts:\n"
    for key, date in shortcuts.items():
        shortcuts_msg += f"[{key}] {date.strftime('%m-%d')}, "
    shortcuts_msg = shortcuts_msg[:-2]

    print(shortcuts_msg)
    date_str = input(prompt + " date (YYYY-MM-DD): ")

    # Check if the input matches any of the shortcuts
    if date_str in shortcuts:
        return shortcuts[date_str]

    # Otherwise, try to parse the input as a date
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD or a valid shortcut.")


def get_time(prompt):
    time_str = input(prompt + " time (HHMM, in 24-h format): ")
    if len(time_str) == 4 and time_str.isdigit():
        try:
            return datetime.strptime(time_str, "%H%M").time()
        except ValueError:
            raise ValueError("Invalid time format. Please use HHMM.")
    else:
        raise ValueError("Invalid time format. Please use HHMM.")


def get_duration(sleep_time, wake_time):
    # assuming a normal sleep duration < 24 hours
    sleep_duration = wake_time - sleep_time
    duration_in_hours = sleep_duration.total_seconds() / 3600
    duration_formatted = f"{duration_in_hours:.2f}" + " hours"
    return duration_formatted


def get_quality():
    sleep_quality = get_input_among_options(
        "\nHow did you feel after the sleep: (a) rested, (b) okay, or (c) tired? Please choose one: ",
        ['a', 'b', 'c'])

    if sleep_quality == "a":
        sleep_quality = "rested"
    elif sleep_quality == "b":
        sleep_quality = "okay"
    else:
        sleep_quality = "tired"
    return sleep_quality


def get_input_among_options(message, options):
    input_value = input(message)
    while True:
        if input_value not in options:
            print(f"Please select one of the options: {options}")
            input_value = input(message)
        else:
            return input_value


def more_sleep_info_to_record():
    print()
    print("I hope you had a great night's sleep.")
    return get_input_among_options(
        "Would you like to add more of your sleep data to our system (Y/N)?",
        ['Y', 'N'])


def summarize_sleep(users_records, user, sleep_time, wake_time, quality):
    sleep_date_str = sleep_time.strftime("%Y-%m-%d")
    sleep_time_str = sleep_time.strftime("%H:%M")
    wake_time_str = wake_time.strftime("%H:%M")

    duration_formatted = get_duration(sleep_time, wake_time)

    sleep_record = {sleep_date_str: [[sleep_time_str, wake_time_str, duration_formatted, quality]]}

    # print('summarize_sleep')
    # print('users_records')
    # pprint.pp(users_records)
    # print('sleep_record')
    # pprint.pp(sleep_record)
    # print('user')
    # pprint.pp(user)

    if user not in users_records:
        users_records[user] = {}
        users_records[user].update(sleep_record)
    else:
        if sleep_date_str in users_records[user].keys():
            users_records[user][sleep_date_str].extend(sleep_record[sleep_date_str])
            users_records[user][sleep_date_str] = sorted(users_records[user][sleep_date_str])
        else:
            users_records[user].update(sleep_record)

    users_records = sort_nested_dict(users_records)

    return users_records
