def deleteAtOddIndex(s):
    output = ""
    for i in range(len(s)):
        if i % 2 == 0:
            output += s[i]
    return output

input_string = "Hello, World!"
result = deleteAtOddIndex(input_string)
print(result)
