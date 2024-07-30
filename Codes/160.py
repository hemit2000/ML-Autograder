def avg(list): 
	sum = 0
	for item in list:
		sum += item 
	return sum / len(list) 

list1 = [7, 8, 10, 4, 11]
result = avg(list1) 
  
print("Average of all items: ", result)
