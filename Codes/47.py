def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            return mid

    return -1

arr = [2, 5, 7, 9, 12, 15]
value = 12
print(binary_search(arr, value))
