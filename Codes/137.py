def longestWord(str):
    words = str.split()
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    for word in words:
        if len(word) == max_len:
            return word

print(longestWord("This is a test string"))
