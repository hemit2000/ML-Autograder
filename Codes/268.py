def even_number_list(a, b):
    return [i for i in range(a, b+1) if i % 2 == 0]

a = 5
b = 10
result = even_number_list(a, b)
print(result)
