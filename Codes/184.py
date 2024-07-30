def merge_lists(l):
    result = []
    for sublist in l:
        for item in sublist:
            result.append(item)
    return result

print(merge_lists([[1, 2, 3], [4, 5], [6]]))
