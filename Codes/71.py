def median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        return (nums[n//2] + nums[(n//2) - 1]) / 2
    return nums[n//2]

nums = [3, 4, 5, 9, 12, 15]
print(median(nums))
