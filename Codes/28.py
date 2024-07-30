def remove_specified_index(lst, index):
    new_list = [lst[i] for i in range(len(lst)) if i != index]

    return new_list

lst = ['Apple', 'Orange', 'Banana', 'Mango']
index = 2

print(remove_specified_index(lst, index))
