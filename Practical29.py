import math

def calculate_area(shape, *args):
    if shape == 'square':
        side = args[0]
        return side**2
    elif shape == 'rectangle':
        length, width = args
        return length * width
    elif shape == 'triangle':
        base, height = args
        return 0.5 * base * height
    elif shape == 'circle':
        radius = args[0]
        return math.pi * radius**2
    elif shape == 'cylinder':
        radius, height = args
        return 2 * math.pi * radius * (radius + height)

# Test the functions
print("Area of square:", calculate_area('square', 5))
print("Area of rectangle:", calculate_area('rectangle', 4, 6))
print("Area of triangle:", calculate_area('triangle', 3, 8))
print("Area of circle:", calculate_area('circle', 4))
print("Surface area of cylinder:", calculate_area('cylinder', 3, 7))
