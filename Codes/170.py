words = "This is an example of a string of words".split()

word_freq = {}
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

for key, value in word_freq.items():
    print(f"{key} : {value}")
