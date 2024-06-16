import collections


def sort_nested_dict(d):
    if not isinstance(d, dict):
        return d
    sorted_dict = collections.OrderedDict()
    for key in sorted(d):
        sorted_dict[key] = sort_nested_dict(d[key])
    return dict(sorted_dict)


def get_duration(sleep_time, wake_time):
    # assuming a normal sleep duration < 24 hours
    sleep_duration = wake_time - sleep_time
    duration_in_hours = sleep_duration.total_seconds() / 3600
    duration_formatted = f"{duration_in_hours:.2f}" + " hours"
    return duration_formatted
