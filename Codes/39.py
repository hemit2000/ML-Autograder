def find_largest_number(numbers):
    if not numbers:
        return None

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [8, 5, 10, 3]
largest = find_largest_number(numbers)
print(largest)
