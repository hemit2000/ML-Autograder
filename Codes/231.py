def max_of_nth(test_list, N):
    res = max([sub[N] for sub in test_list])
    return res

print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))