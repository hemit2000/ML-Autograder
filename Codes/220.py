def isUnique(s):
    chars = []
    for char in s:
        if char in chars:
            return False
        chars.append(char)
    return True

print(isUnique('apple'))
