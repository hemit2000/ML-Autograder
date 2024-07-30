def longest_word_length(words):
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
            
    return length

words = ['Ram', 'Shyam', 'Mohan']
print(longest_word_length(words))
