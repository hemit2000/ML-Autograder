def sum_list(lst1, lst2):
    res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 
    return res_list

print(sum_list([1, 0, 1], [2, 3, 4]))
