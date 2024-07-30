def most_frequent(list): 
    counter = 0
    num = list[0] 

    for i in list: 
        curr_frequency = list.count(i) 
        if curr_frequency > counter: 
            counter = curr_frequency 
            num = i 

    return num

print(most_frequent([1, 2, 3, 4]))
