def replace_vowels(s):
    vowels = 'aeiou'
    for char in vowels:
        s = s.replace(char, 'x')
    return s

print(replace_vowels("hello world"))
