def sum_squares(nums):
    result = 0
    for num in nums:
        result += num * num
    return result

if __name__ == "__main__":
    nums_list = [3, 4, 5]
    result_sum_squares = sum_squares(nums_list)
    print(result_sum_squares)