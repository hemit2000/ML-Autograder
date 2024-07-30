def generate_fibonacci(num_of_elements):
    sequence = []
    a = 0
    b = 1
    for i in range(num_of_elements):
        sequence.append(a)
        c = a + b
        a = b
        b = c
    return sequence

print(generate_fibonacci(10))
