def words_with_four_or_more_characters(my_sentence):
    words = my_sentence.split(" ")
    four_plus_words = []
    for word in words:
        if len(word) >= 4:
            four_plus_words.append(word)
    return four_plus_words

my_sentence = "This is an example sentence"
result = words_with_four_or_more_characters(my_sentence)
print(result)
