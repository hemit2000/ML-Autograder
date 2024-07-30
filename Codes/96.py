def sum_squares(s):
    total = 0
    for x in s:
        total += x * x
    return total

set1 = {1, 2, 3}
result = sum_squares(set1)
print(result)
