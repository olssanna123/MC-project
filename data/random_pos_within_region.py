import numpy as np
import random
from shapely.geometry import Polygon, Point

# coordinates for approximation region as tuples
# North east south west coordinates (latitude, longitude)
Ale = [(58.116472, 12.397922), (57.990763, 12.410281), (57.805393, 12.016147), (58.002408, 12.130130)]

# define polygon
poly = Polygon(Ale)

#Defining the randomization generator
def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)
    return points
# Choose the number of points desired. This example uses 20 points.
points = polygon_random_points(poly,2)
# Printing the results.
#for p in points:
#    print(p.x,",",p.y)

generated_points = []
for p in points:
    x = p.x
    y = p.y
    coord = [x,y]
    generated_points.append(coord)

print(generated_points)