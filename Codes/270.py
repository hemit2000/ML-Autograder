def stringCompress(s):
    result = ""
    counter = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            counter+=1
        else:
            result += s[i] + str(counter)
            counter = 1
        
    result += s[i] + str(counter)
    return result

print(stringCompress('aaabbccccca'))
