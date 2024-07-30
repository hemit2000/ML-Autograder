def replace_elem(lst, val, pos):
    if pos < len(lst):
        lst[pos] = val
    return lst

lst = [1, 2, 3, 4, 5]
element = 8
position = 3

result = replace_elem(lst, element, position)

print('After replacing element:', result)
