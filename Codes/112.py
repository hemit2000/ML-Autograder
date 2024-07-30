def count_ones(binary_string):
    count = 0
    for bit in binary_string:
        if bit == '1':
            count += 1
    return count

binary_string = '10101100110'
print(count_ones(binary_string))
