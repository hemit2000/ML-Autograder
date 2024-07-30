haystack = "Hello World"
needle = "l"

def count_occurrences(haystack, needle):
    count = 0
    for char in haystack:
        if char == needle:
            count += 1
    return count

print(count_occurrences(haystack, needle))
