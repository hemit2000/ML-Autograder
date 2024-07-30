def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1])

tuples = [(1, 3), (2, 1), (3, 2)]
print(sort_tuples(tuples))
