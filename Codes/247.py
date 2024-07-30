def is_key_present(d, x):
    if x in d:
        return True

    return False

print(is_key_present({'a': 100, 'b': 200, 'c': 300}, 'b'))
