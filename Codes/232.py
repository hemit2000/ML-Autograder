def find_common(set_a, set_b):
    return [item for item in set_a if item in set_b]

print(find_common({1, 2, 3}, {2, 3, 4}))