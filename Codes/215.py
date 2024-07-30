import random

def roll_dice():
    dice = random.randint(1, 8)
    return dice

dice = roll_dice()
print(f"You rolled a {dice}")
