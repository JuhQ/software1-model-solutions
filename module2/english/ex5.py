talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

lot_mass = 13.3
pound_lots = 32
talent_pounds = 20

lots_in_grams = lots * lot_mass
pounds_in_grams = pounds * pound_lots * lot_mass
talents_in_grams = talents * talent_pounds * pound_lots * lot_mass

total = lots_in_grams + pounds_in_grams + talents_in_grams

kilograms = int(total / 1000)
grams = total - (kilograms*1000)

print()
print("The weight in modern units:")
print(f"{kilograms: <.0f} kilograms and {grams: <.2f} grams.")
#print(str(kilograms) + " kilograms and " + str(grams) + " grams.")