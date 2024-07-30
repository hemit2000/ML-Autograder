def reverseString(userString):
    wordList = userString.split(" ")
    reversedStringList = list(reversed(wordList))

    return reversedStringList

print(reverseString("The quick brown fox."))
