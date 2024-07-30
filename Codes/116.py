def count_digits(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count

number = 9923
print(count_digits(number))
