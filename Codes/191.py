def is_unique_string(s):
    d = {} 
    for i in s:
        if i in d:
            return False
        d[i] =1
    return True
print(is_unique_string("abcde"))
