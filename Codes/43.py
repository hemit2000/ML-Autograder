def word_count(sentence):
    count = 0
    for word in sentence.split(' '):
        count += 1
    return count

print(word_count("Hey my name is Richard"))
