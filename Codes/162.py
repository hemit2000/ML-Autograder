def average_Even(n) : 
    if (n% 2!= 0) : 
        return ("Invalid Input") 
    sm = 0
    count = 0
    while (n>= 2) : 
        count = count+1
        sm = sm+n 
        n = n-2
    return sm // count 

print(average_Even(10))
