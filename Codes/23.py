def main(num1, num2):
    maximum = max(num1, num2)
    minimum = min(num1, num2)
    
    return maximum, minimum

result = main(5, 10)
print(f"Maximum number: {result[0]}")
print(f"Minimum number: {result[1]}")
