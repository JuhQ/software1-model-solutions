number = int(input("Provide possible prime number: "))

is_prime_number = True

for i in range(2, number):
    if number % i == 0:
        is_prime_number = False
        # print(f"{number} can be divided with {i}")
        # break out of loop immediately, no need to spend CPU-cycles
        break

if is_prime_number:
    print(f"{number} is a prime number :)")
else:
    print(f"{number} is not a prime number :(")