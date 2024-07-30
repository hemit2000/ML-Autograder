def same_charset(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "paris"
str2 = "sapir"
print(same_charset(str1, str2))
