def char_count(str1):
    dict = {} 
    for n in str1: 
        keys = dict.keys() 
        if n in keys: 
            dict[n] += 1
        else: 
            dict[n] = 1 
    return dict
print(char_count("google.com"))
