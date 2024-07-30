def linear_search(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

arr = [2, 3, 5, 7, 11]
n = 11
index = linear_search(arr, n)
print(index)
