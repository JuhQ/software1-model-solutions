import math

def pizza_price_per_m2(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)

    return price / (area / 1000)

print("Pizza 1:")
pizza_1_diameter = float(input("Diameter (cm): "))
pizza_1_price = float(input("Price: "))

print("Pizza 2:")
pizza_2_diameter = float(input("Diameter (cm): "))
pizza_2_price = float(input("Price: "))

pizza1_price_per_m2 = pizza_price_per_m2(pizza_1_diameter, pizza_1_price)
pizza2_price_per_m2 = pizza_price_per_m2(pizza_2_diameter, pizza_2_price)

print(f"pizza1_price_per_m2 = {pizza1_price_per_m2: <.2f}")
print(f"pizza2_price_per_m2 = {pizza2_price_per_m2: <.2f}")

# if the first pizza's price per square meter is lower than the second
if pizza1_price_per_m2 < pizza2_price_per_m2:
    print("Pizza 1 provides better value for money.")
else:
    print("Pizza 2 provides better value for money.")