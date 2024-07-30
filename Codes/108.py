def convert_to_lowercase(string): 
    lowercase_string = "" 
    for char in string: 
        lowercase_string += char.lower() 
    return lowercase_string

print(convert_to_lowercase("HELLO"))
