def gcd(a, b): 
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    a = 28 
    b = 15 
    print(gcd(a, b)) 

if __name__ == "__main__": 
    main()
