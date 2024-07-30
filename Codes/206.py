def find_largest_index(arr):
    largest = float('-inf')
    largest_index = 0
    for i in range(len(arr)):
        num = arr[i]
        if num > largest:
            largest = num
            largest_index = i
    return largest_index 

print(find_largest_index([1,2,3,4,5]))
