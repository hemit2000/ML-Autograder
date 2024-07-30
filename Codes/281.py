string = "mississippi"

def deleteDuplicates(string):
    result = ""
    for i in string:
        if i not in result:
            result += i
    return result

print("The output string is:", deleteDuplicates(string))
