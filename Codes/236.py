def zip_list(list1, list2):
    result = list(map(list.__add__, list1, list2))
    return result

print(zip_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))