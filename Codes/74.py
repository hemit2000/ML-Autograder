def minmax(array):
    max_val = max(array)
    min_val = min(array)
    return [max_val, min_val]

array = [1, 5, 7, 3, 9]
result = minmax(array)
print(result)
