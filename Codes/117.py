def removeDuplicates(list): 
    uniqueList = []  
    for item in list: 
        if item not in uniqueList: 
            uniqueList.append(item) 
    return uniqueList 

print(removeDuplicates([1,4,4,4,5,5,5,6,7]))
