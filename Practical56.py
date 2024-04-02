# Read the lengths of the three sides from the user
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))

# Calculate the surface area of the prism
surface_area = 2 * (a*b + b*c + c*a)

# Print the surface area
print("The surface area of the prism is:", surface_area)
