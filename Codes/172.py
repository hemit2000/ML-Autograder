strings = ['Cat', 'Dog', 'Rabbit', 'Elephant']
n = 5

def filter_strings(strings, n):
    return [s for s in strings if len(s) <= n]

filtered_list = filter_strings(strings, n)
print(filtered_list)
