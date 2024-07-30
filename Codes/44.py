def count_occurrences(string):
    char_count = {}
    for letter in string:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

my_string = 'Hello World!'
letter_occurrences = count_occurrences(my_string)
print(letter_occurrences)
