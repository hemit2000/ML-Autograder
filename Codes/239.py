def index_multiplication(test_tup1, test_tup2):
    res = tuple(tuple(a * b for a, b in zip(tup1, tup2))
                for tup1, tup2 in zip(test_tup1, test_tup2))
    return res

print(index_multiplication(((1, 2, 3), (4, 5, 6), (7, 8, 9)),((1, 2, 3), (4, 5, 6), (7, 8, 9))))