def nth_smallest(input_list, n):
    input_list.sort()
    return input_list[n-1]

input_list = [2, 3, 5, 7, 11]
n = 2
result = nth_smallest(input_list, n)
print(result)
