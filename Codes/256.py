def check_duplicate_in_array(arr):
    result = False
    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            result = True
            break
    return result

arr = [4, 2, 8, 2, 1, 4, 19, 4]
print(check_duplicate_in_array(arr))
