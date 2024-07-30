def isPalindrome(inp):
 inp = inp.lower()
 return inp == inp[::-1]

user_input = input('Enter string: ')
if isPalindrome(user_input):
 print('It\'s a palindrome')
else:
 print('It\'s not a palindrome')
