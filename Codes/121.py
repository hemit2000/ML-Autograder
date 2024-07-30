def unique_strings(strings):
    unique_strings = []
    for string in strings:
        if string not in unique_strings:
            unique_strings.append(string)
    return unique_strings

strings = ["Hello", "World", "Hello", "Python"]
result = unique_strings(strings)
print(result)
