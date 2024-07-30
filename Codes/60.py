def intersection(array_1, array_2):
    result = []
    for num in array_1:
        if num in array_2:
            result.append(num)
    return result

array_1 = [3, 5, 2, 8, 1]
array_2 = [5, 8, 9, 7]
print(intersection(array_1, array_2))  # Outputs: [5, 8]
