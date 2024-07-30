def list_sum(list1, list2):
    total_sum = 0

    for num in list1:
        total_sum += num

    for num in list2:
        total_sum += num

    return total_sum

print(list_sum([1, 2, 3,4], [5, 6, 7, 8]))
