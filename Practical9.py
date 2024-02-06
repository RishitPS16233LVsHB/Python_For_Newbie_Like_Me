import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Radius values
radii = [7, 12, 16]

# Calculate and print volume for each radius
for radius in radii:
    volume = sphere_volume(radius)
    print(f"The volume of a sphere with radius {radius} cm is {volume:.2f} cubic cm.")
