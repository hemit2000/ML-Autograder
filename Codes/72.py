def difference(string1, string2):
    new_string = ''
    for char in string2:
        if char not in string1:
            new_string += char
    return new_string

string1 = 'jello'
string2 = 'hello'
print(difference(string1, string2))
