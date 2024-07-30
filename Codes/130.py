def replace_numbers(arr):
    for i, num in enumerate(arr):
        if num > 5:
            arr[i] = 0

arr = [1, 4, 6, 7, 8, 9]
replace_numbers(arr)
print(arr)
