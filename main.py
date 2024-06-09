# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime

users_records = {}


def main():
    user_name = get_user_info()
    date_recorded = get_date()
    sleep_time_recorded = get_sleep_time()
    wake_time_recorded = get_wake_time()
    quality_recorded = get_quality()
    sleep_records = summarize_time(date_recorded, sleep_time_recorded, wake_time_recorded, quality_recorded)
    # print_summary(user_name, date_recorded, sleep_time_recorded, wake_time_recorded, quality_recorded)
    summarize_user(user_name, sleep_records)

def get_user_info():
    user_id = input("Please type in your name: ")
    print(user_id)
    return user_id

def get_date():
    print("Please type in the date you would like to record...")
    year_to_record = int(input("Year: "))
    month_to_record = int(input("Month: "))
    day_to_record = int(input("Day: "))
    # Create a date object
    date_obj = datetime.date(year_to_record, month_to_record, day_to_record)
    # Convert the date object to a string in yyyy-mm-dd format
    formatted_date = date_obj.strftime("%Y-%m-%d")
    print(formatted_date)
    return formatted_date

def get_time():
    hour_to_record = int(input("Hour: "))
    minute_to_record = int(input("Minute: "))
    time_obj = datetime.time(hour_to_record, minute_to_record)
    formatted_time = time_obj.strftime("%H:%M")
    return formatted_time

def get_sleep_time():
    print("Please type in your sleep time...")
    sleep_time = get_time()
    print(sleep_time)
    return sleep_time

def get_wake_time():
    print("Please type in your wake time...")
    wake_time = get_time()
    print(wake_time)
    return wake_time

def get_quality():
    sleep_quality = input("How did you feel after the sleep: (a) rested, (b) okay, or (c) tired? Please choose one: ")
    while True:
        if sleep_quality  not in ['a', 'b', 'c']:
            print("Please enter a, b, or c.")
            sleep_quality = input("How did you feel after the sleep: (a) rested, (b) okay, or (c) tired? ")
        else:
            if sleep_quality == "a":
                sleep_quality = "rested"
            elif sleep_quality == "b":
                sleep_quality = "okay"
            else:
                sleep_quality = "tired"
            print(sleep_quality)
            return sleep_quality

def get_additional_input():
    choice = input("Do you want to add more records (Y/N)? ")
    while True:
            if choice not in ['Y', 'N']:
                choice = input("Please input 'Y' or 'N'. ")
            else:
                if choice == 'Y':
                    date_added = get_date()
                    sleep_added = get_sleep_time()
                    wake_added = get_wake_time()
                    quality_added = get_quality()
                    print(date_added, sleep_added, wake_added, quality_added)
                    return date_added, sleep_added, wake_added, quality_added
                else:
                    print("Thank you!")

# def is_same_day(a, b):
#     if a == b:
#         sleep_total =
#         return sleep_total

def summarize_time(date, sleep_time, wake_time, quality):
    sleep_records = {}
    sleep_times = []

    sleep_times.append(sleep_time)
    sleep_times.append(wake_time)
    sleep_times.append(quality)
    sleep_records[date] = sleep_times
    print(sleep_records)
    return sleep_records

def summarize_user(user, sleep_record):
    users_records[user] = sleep_record
    print(users_records)
    return users_records

# def print_summary(a, b, c, d, e):
#     # (create in other functions)
#     # and store the data in a dictionary, and print the results via 'for' loop
#     print(f"{a} had slept for xxx from {c} to {d} on {b}, and felt {e}.")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
