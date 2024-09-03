# 1 inch = 2.54 cm

inch = float(input("Provide inches: "))

while inch >= 0:
    print(f"{inch} inches is {inch * 2.54} cm.")
    inch = float(input("Provide inches: "))

# print(inch)
"""
while True:
    inch = float(input("Provide inches: "))
    if inch < 0:
        break

    print(f"{inch} inches is {inch * 2.54} cm.")
"""