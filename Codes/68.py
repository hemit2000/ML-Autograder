def print_divisors(input):

    for i in range(1, input + 1):
        if input % i == 0:
            print (i)

input = 28

print_divisors(input)
