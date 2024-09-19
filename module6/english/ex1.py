import random

def random_dice():
    return random.randint(1,6)

while True:
    roll = random_dice()
    print(f"Roll: {roll}")
    if roll == 6:
        break
