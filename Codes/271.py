def alphabet_order(sentence):
    output = ""
    for character in sentence:
        if character.isalpha():
            ascii_value = ord(character)
            ascii_value += 1
            output += chr(ascii_value)
        else:
            output += character
    return output

print(alphabet_order("Hello, World!"))
