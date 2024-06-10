import collections


def sort_nested_dict(d):
    if not isinstance(d, dict):
        return d
    sorted_dict = collections.OrderedDict()
    for key in sorted(d):
        sorted_dict[key] = sort_nested_dict(d[key])
    return dict(sorted_dict)
