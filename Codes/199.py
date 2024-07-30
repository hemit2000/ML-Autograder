def find_largest_sum(list):
    largestNum = max(list)
    list.remove(largestNum)
    secondLargestNum = max(list)
    return largestNum+secondLargestNum

print(find_largest_sum([1,2,3,4,5]))
