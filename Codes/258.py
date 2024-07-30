def move_last_3(list):
    last3 = list[-3:]
    del list[-3:]
    list = last3 + list
    return list

print(move_last_3([1, 2, 3, 4, 5, 6, 7, 8, 9]))