def sort_list_by_length(list_of_strings):
    return sorted(list_of_strings, key=len)

list_of_strings = ["Python", "is", "a", "programming", "language"]
sorted_list = sort_list_by_length(list_of_strings)

print(sorted_list)
