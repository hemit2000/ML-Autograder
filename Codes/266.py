def flatten_dictionary(d):
    result = {}

    def traverse(k, v):
        if isinstance(v, dict):
            for k1, v1 in v.items():
                traverse(k+"."+k1, v1)
        else:
            result[k] = v

    traverse("", d)

    return result

print(flatten_dictionary({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}))