list_of_strings = ["I", "am", "so", "happy"]

longest_string_len = 0
for string in list_of_strings:
    if len(string) > longest_string_len:
        longest_string_len = len(string)

print(longest_string_len)
