def find_index(arr, num):
    for index in range(len(arr)):
        if arr[index] == num:
            return index
    return -1

arr = [1, 3, 7, 9, 0, 4]
num = 7
index = find_index(arr, num)
print(f'Index of {num} is {index}')
