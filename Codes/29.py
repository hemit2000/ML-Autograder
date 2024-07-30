import string

input_str = "This is a cool string!"
punctuation_removed = input_str.translate(str.maketrans('', '', string.punctuation))
print(punctuation_removed)
