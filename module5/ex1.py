import random
roll_count = int(input("Give roll count: "))
total = 0

for i in range(roll_count):
    total = total + random.randint(1, 6)

print(f"Total sum: {total}")
