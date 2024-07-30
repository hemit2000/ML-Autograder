def join_list_with_separator(lst, separator):
    joined_string = separator.join(lst)
    return joined_string

lst = ["Hello", "World!"]
separator = " "
result = join_list_with_separator(lst, separator)
print(result)
