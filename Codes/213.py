def merge_strings(string_1, string_2):
    s = set(string_1 + string_2)
    merged_string = ''.join(s)
    return merged_string

string_1 = 'one'
string_2 = 'two'
merged_string = merge_strings(string_1, string_2)
print(merged_string)
