def reverse_number(num):
    rev = 0
    while num > 0:
        reminder = num%10
        rev = (rev*10)+reminder
        num = num//10
    return rev
print(reverse_number(12345))
