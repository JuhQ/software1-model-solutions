length = float(input("Give length of Zander in centimeters: "))

min_length = 42

if length < min_length:
    print(f"Return the fish to the water. The minimum length of Zander is {min_length}, this Zander is undersized. Needs to be {min_length - length} cm longer.")
else:
    print("This is ok. The min size for Zander is " + str(min_length) + " centimers. " + str(length) + " cm exceeds the minimum requirement.")
