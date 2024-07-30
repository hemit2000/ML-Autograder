def split_array_sum(arr):
    sum_arr = sum(arr)
    half_sum = sum_arr / 2
    current_sum = 0
    left_index = 0

    for index, value in enumerate(arr):
        current_sum += value
        if current_sum >= half_sum:
            left_index = index
            break

    left_arr = arr[:left_index + 1]
    right_arr = arr[left_index + 1:]
    return left_arr, right_arr

arr = [1, 2, 3, 4, 5, 6]
left_arr, right_arr = split_array_sum(arr)
print("Left array:", left_arr)
print("Right array:", right_arr)
