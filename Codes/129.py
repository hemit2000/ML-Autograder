def filter_words_with_a(words):
    return [word for word in words if 'a' in word]

words = ['dog', 'cat', 'ant', 'tree', 'apple']
filtered_words = filter_words_with_a(words)
print(filtered_words)
