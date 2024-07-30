def find_index(my_list, value):
    for i in range(len(my_list)):
        if my_list[i] == value:
            return i
    return -1

my_list = [2, 4, 6, 8]
value = 4
index = find_index(my_list, value)
print(index)
