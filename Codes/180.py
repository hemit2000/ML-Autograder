def remove_words(word, words):
    return [w for w in words if w != word]

word = 'Hello'
words = ['Hi', 'there', 'Hello', 'Goodbye']

result = remove_words(word, words)
print(result)
