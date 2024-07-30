def is_prime(num): 
    if num > 1: 
        for i in range(2, num): 
            if (num % i) == 0: 
                return False 
        else: 
            return True
    else: 
        return False

numbers = [2, 4, 7, 11, 13]   
for num in numbers: 
    if is_prime(num): 
        print(num)
