from collections import Counter 
def count_Occurrence(tup, lst): 
    count = 0
    for item in tup: 
        if item in lst: 
            count+= 1 
    return count  

print(count_Occurrence((1,2,3,4,5), [1,2,3,4,5,6,7,8,9,10]))
