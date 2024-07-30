from collections import Counter

sentence = "This is a test sentence"

words = sentence.split()

word_frequency = Counter(words)

print(word_frequency)
