def find_even_odd(nums):
    even_list = []
    odd_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
  
    return even_list, odd_list
  
print(find_even_odd([1, 2, 3, 4, 5, 6]))
