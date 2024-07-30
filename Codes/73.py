def count_words(input_string):
    words_count = {}
    words = input_string.split()
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count

input_string = "This is an example of a string."
words_count = count_words(input_string)
print(words_count)
