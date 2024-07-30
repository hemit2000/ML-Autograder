def format_string(string):
    formatted_string = string.capitalize()
    
    if not formatted_string.endswith(('.', '!', '?')):
        formatted_string += '.'
    
    return formatted_string

string = "hello, world"
formatted = format_string(string)
print(formatted)
