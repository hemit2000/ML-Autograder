def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return i
        left_sum += num
    return -1

print(equilibrium_index([1, 2, 3, 4, 5, 4, 2, 2]))
