import math

# circle radius
radius = float(input("Give circle radius: "))

area = math.pi * (radius ** 2)

#print("Area = " + str(area))
print(f"Area = {area: <5.3f}")