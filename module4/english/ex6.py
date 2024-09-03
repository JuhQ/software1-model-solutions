import random

number_of_points = 100000

counter = 0
points_inside_circle = 0

while counter < number_of_points:
    counter = counter + 1

    x = random.randint(-1000, 1000) / 1000
    y = random.randint(-1000, 1000) / 1000

    if x ** 2 + y**2 < 1:
        points_inside_circle = points_inside_circle + 1

print(f"Pi: {(points_inside_circle / number_of_points) * 4 }")


#solution 2: 

random_points = int(input("How many random points to generate?")) 
inside_points = 0                                                 
i = 0                                                
while i < random_points:                                         
    x = random.uniform(-1., 1.)    
    y = random.uniform(-1., 1.)    
    if x**2 + y**2 < 1.:           
        inside_points = inside_points + 1

    i = i + 1
pi = 4.* inside_points/random_points                       
print(f"Pi is {pi}, error {math.pi - pi}")
