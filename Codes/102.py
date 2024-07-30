def find_frequencies(sample_string):
    frequency_table = dict()
    for char in sample_string:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    return frequency_table

sample_string = "HelloWorld"
result = find_frequencies(sample_string)
print(result)
