def findSum(nums, value):
    total = 0

    for num in nums:
        if num > value:
            total += num

    return total

nums = [1, 4, 5, 10, 12]
value = 6

res = findSum(nums, value)

print(res)
