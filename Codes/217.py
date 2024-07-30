def next_largest_palindrome(num):
    num = int(num)
    num += 1
    while not is_palindrome(str(num)):
        num += 1

    return num

def is_palindrome(num):
    return num == num[::-1]

print(next_largest_palindrome("1234"))
