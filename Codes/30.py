def highest_value(d):
    key, highest_val = None, -float("inf")
    for k, val in d.items():
        if val > highest_val:
            key, highest_val = k, val
    return key

highest_key = highest_value( d = {
    'a': 1,
    'b': 5,
    'c': 3
})
print(highest_key)
