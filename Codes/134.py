def splitOnWhitespace(inputString):
    words = inputString.split()
    return words

stringToBeSplit = "Python is an interpreted language."
words = splitOnWhitespace(stringToBeSplit)
print(words)
