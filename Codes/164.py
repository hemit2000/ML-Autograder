sentence = "This is a sample sentence"
length = 4

def count_long_words(sentence, length):
    words = sentence.split()
    count = 0
    
    for word in words:
        if len(word) > length:
            count += 1
    return count

result = count_long_words(sentence, length)
print(result)
