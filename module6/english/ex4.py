
def sum_values(values):
    total = 0
    for value in values:
        total = total + value
    return total


values = []
while True:
    user_input = input("Provide value (empty value ends program): ")
    if user_input == "":
        break

    value = int(user_input)
    values.append(value)

print(f"Sum: {sum_values(values)}")