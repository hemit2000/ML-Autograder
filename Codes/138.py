def append_first_letter_end(list_of_strings):
    new_list_of_strings = []
    for string in list_of_strings:
        new_string = string + string[0]
        new_list_of_strings.append(new_string)
    return new_list_of_strings

print(append_first_letter_end(["cat", "bird", "rabbit"]))
