year = int(input("Give year: "))

# rules of leap year
# year can be divided by four
# 100 valid only if also divisible by 400

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

"""
year = int(input("Give year: "))

# rules of leap year
# year can be divided by four
# 100 valid only if also divisible by 400

divisible_by_four = year % 4 == 0
divisible_by_400 = (year % 100 != 0 or year % 400 == 0)

if divisible_by_four and divisible_by_400:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
"""