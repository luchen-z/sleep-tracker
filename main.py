# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime

users_records = {}


def main():
    while has_sleep_info_to_record() == "Y":
        user_name = get_user_info()
        get_sleep_info(user_name)
        print(users_records)

    print("Thank you.")
    exit()


def get_sleep_info(user):
    sleep_time_recorded = get_date_and_time("Sleep")
    wake_time_recorded = get_date_and_time("Wake")
    sleep_duration = get_duration(sleep_time_recorded, wake_time_recorded)
    quality_recorded = get_quality()
    return summarize_sleep(user, sleep_time_recorded, wake_time_recorded, sleep_duration, quality_recorded)


def get_user_info():
    user_id = input("Please type in your name: ")
    print(user_id)
    return user_id


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
    # assuming a normal sleep duration < 24 hours;
    # If the sleep crosses midnight, we will record two blocks of duration set apart by midnight
    # if wake_time >= sleep_time:
    #     pass
    # else:
    #     sleep_time = sleep_time - datetime.timedelta(days=1)
    sleep_duration = wake_time - sleep_time
    return sleep_duration


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


def summarize_sleep(user, sleep_time, wake_time, duration, quality):

    sleep_date_str = sleep_time.strftime("%Y-%m-%d")
    sleep_time_str = sleep_time.strftime("%H:%M")
    wake_date_str = wake_time.strftime("%Y-%m-%d")
    wake_time_str = wake_time.strftime("%H:%M")

    if sleep_time.date() != wake_time.date():
        intermediate_time = wake_time.replace(hour=0, minute=0)
        pre_mid_duration = (intermediate_time - sleep_time).total_seconds() / 3600
        post_mid_duration = (wake_time - intermediate_time).total_seconds() / 3600
        pre_mid_duration_formatted = f"{pre_mid_duration:.2f}" + " hours"
        post_mid_duration_formatted = f"{post_mid_duration:.2f}" + " hours"

        intermediate_time_str = intermediate_time.strftime("%H:%M")

        sleep_record = {sleep_date_str: [[sleep_time_str, intermediate_time_str, pre_mid_duration_formatted, quality]],
                        wake_date_str: [[intermediate_time_str, wake_time_str, post_mid_duration_formatted, quality]]}
    else:
        duration = duration.total_seconds() / 3600
        duration_formatted = f"{duration:.2f}" + " hours"

        sleep_record = {sleep_date_str: [[sleep_time_str, wake_time_str, duration_formatted, quality]]}

    if user not in users_records:
        users_records[user] = {}
        users_records[user].update(sleep_record)
    else:
        if sleep_date_str in users_records[user].keys():
            users_records[user][sleep_date_str].extend(sleep_record[sleep_date_str])
        elif wake_date_str in users_records[user].keys():
            users_records[user][wake_date_str].extend(sleep_record[wake_date_str])
        else:
            users_records[user].update(sleep_record)

    return users_records


# def save_user_sleep_record(user, sleep_record):
#     users_records[user] = sleep_record
#     print(users_records)
#     return users_records


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
