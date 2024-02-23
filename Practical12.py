import math

def compute_height(length, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    height = length * math.sin(angle_radians)
    return height

ladder_data = [(16, 75), (20, 0), (24, 45), (24, 80)]

for length, angle in ladder_data:
    height = compute_height(length, angle)
    print(f"For a ladder of length {length} feet and angle {angle} degrees, the height reached is {height:.2f} feet.")
