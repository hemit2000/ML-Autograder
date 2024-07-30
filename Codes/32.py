def find_max(arr, n):
    max_value = arr[0]

    for i in range(1, n):

        if arr[i] > max_value:
            max_value = arr[i]

    return max_value

arr = [1, 6, 8, 4, 9, 6, 10]
n = len(arr)
print(find_max(arr, n))
