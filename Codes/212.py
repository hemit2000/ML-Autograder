def sort_dictionary_keys(d):
    return {k: d[k] for k in sorted(d.keys(), reverse=True)}

d = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}

sorted_dict = sort_dictionary_keys(d)
print(sorted_dict)
