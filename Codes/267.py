def calculate_median(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        mid1 = len(nums) // 2
        mid2 = mid1 - 1
        return (nums[mid1] + nums[mid2]) / 2
    
    return nums[len(nums) // 2]

nums = [3, 5, 10, 2]
print(calculate_median(nums))
