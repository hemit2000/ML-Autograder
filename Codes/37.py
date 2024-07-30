def compute_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

numbers = [4, 8, 6, 2, 10]
average = compute_average(numbers)
print(average)
