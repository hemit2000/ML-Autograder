import random

def generate_random_password(characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}:"):
    password = ""
    for _ in range(8):
        password += random.choice(characters)
    return password

print(generate_random_password())
