def intersection(a, b): 
    intersection_list = []
    for item1 in a:
        if item1 in b:
            intersection_list.append(item1)
    return intersection_list

a = [1, 5, 8, 9, 10]
b = [2, 3, 5, 8, 9, 10]
print(intersection(a, b))
