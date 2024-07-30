import random

def roll_dice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_sum = roll1 + roll2
    print(f"You rolled {roll1} and {roll2}. The total is {roll_sum}, which is {'even' if roll_sum % 2 == 0 else 'odd'}.")
    
roll_dice()
