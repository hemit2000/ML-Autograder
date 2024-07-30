def filter_long_strings(string_list):
    long_strings = []
    for string in string_list:
        if len(string) > 5:
            long_strings.append(string)
    return long_strings

string_list = ['Python', 'is', 'Fun']

long_strings = filter_long_strings(string_list)
print(long_strings)
