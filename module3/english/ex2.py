cabin_class = input("Provide cabin class (LUX, A, B, C): ")

if cabin_class == "LUX":
    print("LUX is upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A is above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B is windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C is windowless cabin below the car deck.")
else:
    print("Invalid cabin class")