import datetime
import pprint


def split_record_if_overnight(sleep_time_recorded, wake_time_recorded):
    if sleep_time_recorded.date() != wake_time_recorded.date():
        intermediate_time = wake_time_recorded.replace(hour=0, minute=0)
        return [[sleep_time_recorded, intermediate_time],
                [intermediate_time, wake_time_recorded]]
    else:
        return [[sleep_time_recorded, wake_time_recorded]]


def get_sleep_info():
    # Input phase
    sleep_time_recorded = get_date_and_time("Sleep")
    wake_time_recorded = get_date_and_time("Wake")
    quality_recorded = get_quality()

    # Split the sleep record if it is overnight
    sleep_records = split_record_if_overnight(sleep_time_recorded, wake_time_recorded)

    return [sleep_records, quality_recorded]


def get_user_info():
    user_id = input("Please type in your name: ")
    return user_id.strip()


def get_date_and_time(prompt):
    print("Please enter your " + str(prompt).lower() + " date and time...")
    while True:
        try:
            date_str = input(prompt + " date (YYYY-MM-DD): ")
            time_str = input(prompt + " time (HH:MM, in 24-h format): ")
            datetime_str = date_str + " " + time_str
            datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            return datetime_obj
        except ValueError:
            print("Invalid date or time format. Please enter the date in YYYY-MM-DD and time in HH:MM format.")


def get_duration(sleep_time, wake_time):
    # assuming a normal sleep duration < 24 hours
    sleep_duration = wake_time - sleep_time
    duration_in_hours = sleep_duration.total_seconds() / 3600
    duration_formatted = f"{duration_in_hours:.2f}" + " hours"
    return duration_formatted


def get_quality():
    sleep_quality = get_input_among_options(
        "How did you feel after the sleep: (a) rested, (b) okay, or (c) tired? Please choose one: ",
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


def has_sleep_info_to_record():
    return get_input_among_options(
        "Hi, I hope you had a wonderful sleep. Do you want to record your sleep stats into our system (Y/N)? ",
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
        else:
            users_records[user].update(sleep_record)

    return users_records
