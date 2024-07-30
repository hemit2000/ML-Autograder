def is_in_range(n, lower, upper):
    return True if lower <= n & n <= upper else False

print(is_in_range(3, 1, 10))