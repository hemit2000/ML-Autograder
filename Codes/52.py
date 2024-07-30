import sys

if len(sys.argv) != 3:
    print("Usage: python 52.py <number1> <number2>")
    sys.exit(1)

try:
    number1 = float(sys.argv[1])
    number2 = float(sys.argv[2])
    result = number1 * number2
    print("The multiplication result is:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
