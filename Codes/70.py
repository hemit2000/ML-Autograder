def sum_positivenum(nums):
    positive_nums = list(filter(lambda x: x > 0, nums))
    return sum(positive_nums)

nums = [1, -2, 3, -4, 5]
result = sum_positivenum(nums)
print(result)
