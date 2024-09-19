import random

def random_dice(max):
    return random.randint(1,max)

maximum_sides = input("Give maximum sides: ")

# prevent crashing if user provides empty value
# consider empty value to represent value 6
if maximum_sides == "":
    maximum_sides = 6
else:
    maximum_sides = int(maximum_sides)

while True:
    roll = random_dice(maximum_sides)
    print(f"Roll {roll}")
    if roll == 6:
        break
