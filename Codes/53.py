def search(list_tmp, value):
    for index, item in enumerate(list_tmp):
        if item == value:
            return index

    return -1

list_tmp = [1, 23, 42, 5, 7, 34, 89]
value = 42
index = search(list_tmp, value)
print(index)
