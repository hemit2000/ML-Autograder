import random

names = ["John", "Andy", "Alex", "Paul", "Pippa"]

def getRandomName(names):
    randomIndex = random.randint(0, len(names)-1) 
    return names[randomIndex]

if __name__ == '__main__':
    print(getRandomName(names))
