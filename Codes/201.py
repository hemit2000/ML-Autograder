from collections import Counter

text = " Python is a high-level programming language."
words = text.split()

frequencies = Counter(words)

frequent_words = frequencies.most_common(5)

print(frequent_words)
