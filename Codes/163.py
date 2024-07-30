def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for char in text:
        if char.lower() not in vowels:
            result += char
    return result

text = "example text"
print(remove_vowels(text))
