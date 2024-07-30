def checkArmstrong(num):
    temp = num 
    res = 0
    while temp > 0: 
        digit = temp % 10
        res = res + digit ** 3
        temp = temp // 10
    
    if num == res: 
        return f'{num} is an Armstrong Number'
    else:
        return f'{num} is not an Armstrong Number'
    
print(checkArmstrong(153))
