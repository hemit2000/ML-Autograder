def count_Pairs(arr,n): 
    cnt = 0
    for i in range(n): 
        for j in range(i + 1,n): 
            if arr[i] == arr[j]: 
                cnt += 1 
    return cnt 

print(count_Pairs([1,2,3,1,1,3],6))