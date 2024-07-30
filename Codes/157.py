def find_factors(num): 
    """Function to find prime factors"""
    factors = [] 
    i = 2
    while i * i <= num: 
        if num % i: 
            i += 1 
        else: 
            num //= i 
            factors.append(i) 
    if num > 1: 
        factors.append(num) 
    return factors 
  
num = 15
print(find_factors(num))
