def clean_string(string):
    excluded_characters = "*&#$@!"
    cleaned_string = ''
    for character in string:
        if character not in excluded_characters:
            cleaned_string += character
    return cleaned_string

print(clean_string("H*em&it"))