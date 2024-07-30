def sum_odd_numbers(nums):
    result = 0
    for num in nums:
        if num % 2 != 0:
            result += num
    return result

result = sum_odd_numbers([1, 2, 3, 4, 5])
print(result)
