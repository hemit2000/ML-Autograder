import string
import random

def generate_password(length):
    charPool = string.ascii_letters + string.digits
    password = ''.join(random.sample(charPool, length))
    return password

password = generate_password(8)
print(password)
