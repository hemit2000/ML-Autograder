def find_largest_word(sentence):
    splits = sentence.split(' ')
    largest_word = ""
    for word in splits:
        if len(word) > len(largest_word):
            largest_word = word
    return largest_word

print(find_largest_word("This sentence has seven words."))
