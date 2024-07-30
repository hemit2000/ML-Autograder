def has_duplicates(arr): 
    s = set() 

    for item in arr: 
        if item in s:
            return True 
        else:
            s.add(item) 

    return False

print(has_duplicates([1,2,3,4,5,6,7,8,9,10]))
