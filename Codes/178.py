import re

def delete_pattern_characters(string, pattern):
    return re.sub(pattern, '', string)

string = "The quick brown fox jumps over the lazy dog."
pattern = r'q[a-z]ck'

result = delete_pattern_characters(string, pattern)
print(result)
