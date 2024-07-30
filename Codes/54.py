def remove_duplicates(list_of_lists):
    result = []
    for item in list_of_lists:
        if item not in result:
            result.append(item)
    result.sort()
    return result

list_of_lists = [['b', 'a', 'd'], ['c', 'a', 'd'], ['a', 'f', 'g']]
print(remove_duplicates(list_of_lists))
