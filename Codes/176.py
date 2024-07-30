def Split(list): 
    ev_li = [] 
    for i in list: 
        if (i % 2 == 0): 
            ev_li.append(i)  
    return ev_li

print(Split([1, 2, 3, 4, 5, 6, 7, 8, 9]))
