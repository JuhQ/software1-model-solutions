
gallon_in_liters = 3.785

def gallons_to_liters(gallons):
    return gallons * gallon_in_liters

while True:
    gallons = input("Give gallons: ")

    if gallons == "":
        print("Empty value, breaking out of loop.")
        break

    if float(gallons) < 0:
        print("Negative value, breaking out of loop.")
        break

    print(gallons_to_liters(float(gallons)))