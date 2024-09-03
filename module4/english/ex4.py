import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess: "))

    if guess == number:
        print("Correct")
        break

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")