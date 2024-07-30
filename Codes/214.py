def new_tuple(test_list, test_str):
    res = tuple(test_list + [test_str])
    return res

print(new_tuple([1, 2, 3], 'Hello'))
