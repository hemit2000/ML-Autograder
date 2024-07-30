def count_char(string, char):
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1
    return count

string = "hello"
char = "l"
result = count_char(string, char)
print(f"The character '{char}' appears {result} times in '{string}'.")  # Output: The character 'l' appears 2 times in 'hello'.
