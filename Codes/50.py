def find_longest_string(arr):
    longest_string = ''
    for s in arr:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string

# Example usage
arr = ["Apple", "Banana", "Orange", "Mango", "Pineapple"]
result = find_longest_string(arr)
print('Longest string is', result)
