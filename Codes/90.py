def find_Extra(arr1,arr2,n) : 
    for i in range(0, n) : 
        if (arr1[i] != arr2[i]) : 
            return i 
    return n 

print(find_Extra([2, 4, 6, 8, 9, 10, 12], [2, 4, 6, 8, 10, 12], 7))
