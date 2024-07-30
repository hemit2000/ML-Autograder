def median(nums):
    nums.sort()
    length = len(nums)
 
    if length % 2 == 0:
        return (nums[length//2] + nums[(length//2)-1])/2.0
    else:
        return nums[length//2] 

list = [5, 8, 2, 7, 4]
med = median(list)
print('The median of the list is ' + str(med))
