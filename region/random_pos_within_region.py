import numpy as np
import random
from shapely.geometry import Polygon, Point

def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)
    return points

def random_point_within_region(region):
    poly = Polygon(region)
    point = polygon_random_points(poly,1)
    x = point[0].x
    y = point[0].y
    coord = [x,y]
    return coord

def several_random_points_within_region(region, num_points):
    poly = Polygon(region)
    points = polygon_random_points(poly,num_points)
    generated_points = []
    for p in points:
        x = p.x
        y = p.y
        coord = [x,y]
        generated_points.append(coord)
    return generated_points
