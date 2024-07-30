def top_three(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[:3]

print(top_three([7, 13, 5, 8, 50, 11, 64, 48]))
