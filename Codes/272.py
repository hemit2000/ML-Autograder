import random

def generate_random_words(n):
    words = ["hello", "world", "foobar", "python", "code"]
    output = ""

    for _ in range(n):
        output += random.choice(words)
        output += " "

    return output[:-1]

print(generate_random_words(5))