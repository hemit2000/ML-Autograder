def sort_dict_by_values(my_dict):
    return sorted(my_dict.items(), key=lambda kv: kv[1])

print(sort_dict_by_values({'a': 1, 'b': 2, 'c': 3}))