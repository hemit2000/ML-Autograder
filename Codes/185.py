def romanToInt(s):
    values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

    number = 0
    for i in range(len(s)):
        if i == 0 or values[s[i]] <= values[s[i-1]]:
            number += values[s[i]]
        else:
            number += values[s[i]] - 2*values[s[i-1]]

    return number

print(romanToInt('III'))
