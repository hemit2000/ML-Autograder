def longer_string(string1, string2):
    if len(string1) > len(string2):
        return string1
    return string2

string1 = 'cat'
string2 = 'dog'
result = longer_string(string1, string2)
print(f"The longer string is: {result}")
