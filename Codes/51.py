def odd_numbers(n): 
    odd_numbers = [] 
       
    for i in range(1, n + 1): 
        if i % 2 != 0: 
            odd_numbers.append(i) 
    return odd_numbers
print(odd_numbers(10))
