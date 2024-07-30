def common_characters(str1, str2):
    common_chars = set(str1).intersection(set(str2))
    return list(common_chars)

print(common_characters('apple', 'orange'))