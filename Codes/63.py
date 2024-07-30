def filter_list(lst):
    seen = set()
    filtered_list = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            filtered_list.append(item)
    
    return filtered_list

my_list = [1, 2, 2, 3, 3, 4]
filtered_list = filter_list(my_list)
print(filtered_list)
