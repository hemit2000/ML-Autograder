def string_to_length(list_strings):
    return [len(string) for string in list_strings]

list_strings = ["Hello", "World", "Goodbye"]
lengths = string_to_length(list_strings)
print(lengths)
