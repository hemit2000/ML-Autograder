def find_max_element(arr):
    maxElement = arr[0]
    for val in arr:
        if val > maxElement:
            maxElement = val
    return maxElement

print(find_max_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
