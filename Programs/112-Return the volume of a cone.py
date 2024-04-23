# Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth.
# V = 1/3пr**2h
# Examples
# cone_volume(3, 2) ➞ 12.57
# cone_volume(15, 6) ➞ 565.49
# cone_volume(18, 0) ➞ 0

import math

def cone_volume(height, radius):
    if radius == 0:
        return 0
    volume = (1/3) * math.pi * (radius**2) * height
    return round(volume, 2)

print (cone_volume(3, 2))
print(cone_volume(18, 0))