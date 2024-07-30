def filter_numeric(input_list): 
    
    num_list = [] 
  
    for item in input_list:
        if type(item) == int or type(item) == float: 
            num_list.append(item) 
   
    return num_list 
  
input_list = [4, 2, 1, 15.6, 'p', 'y', 5.8] 
print(filter_numeric(input_list)) 
