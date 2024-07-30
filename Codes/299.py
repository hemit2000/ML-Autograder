def leftRotate(arr, k):
    n = len(arr)
    k = k % n
    new_arr = arr[k:] + arr[:k]
    return new_arr

arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = leftRotate(arr, k)
print(rotated_arr)
