def prime_numbers(x, y):
    prime_nums = {}

    for i in range(x, y + 1):
        if i > 1:
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_nums[i] = i

    return prime_nums

print(prime_numbers(8, 20))
