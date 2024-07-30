def remove_word(sentence, word):
    words = sentence.split()
    new_words = [w for w in words if w != word]
    return ' '.join(new_words)

sentence = "I love learning Python but sometimes it is hard to understand"
new_sentence = remove_word(sentence, 'Python')
print(new_sentence)
