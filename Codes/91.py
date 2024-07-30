sentence = "I am going to the store to buy food"

words = sentence.split(' ')

# Table to keep track of duplicates
table = []

for word in words:
    if word in table:
        print("Duplicate word found: " + word)
    else:
        table.append(word)
