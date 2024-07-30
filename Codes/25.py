def Fibonacci_Sequence(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci_Sequence(n-1)+Fibonacci_Sequence(n-2) 
  
print(Fibonacci_Sequence(10))
