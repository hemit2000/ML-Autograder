def list_multiplication(nums):
    output_list = []
    for i in range(len(nums)):
        output_list.append(nums[i] * 2)
    return output_list

nums = [3, 5, 8, 9]
result = list_multiplication(nums)
print(result)
