user_input = input("Provide value: ")
number = int(user_input)

smallest = number
largest = number

while True:
    value = input("Provide value: ")
    if value == "":
        break

    number = int(value)

    if number < smallest:
        smallest = number
    if number > largest:
        largest = number

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")