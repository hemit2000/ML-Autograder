def isAnagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    n1 = len(str1)
    n2 = len(str2)
    
    if n1 != n2:
        return False
    
    str1_sorted = ''.join(sorted(str1))
    str2_sorted = ''.join(sorted(str2))
    
    for i in range(n1):
        if str1_sorted[i] != str2_sorted[i]:
            return False
    
    return True

string1 = "army"
string2 = "mary"
result = isAnagram(string1, string2)
print(result)
