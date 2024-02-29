def calculate_determinant(a, b, c):
    determinant = b**2 - 4*a*c
    if determinant > 0:
        return "Positive determinant"
    elif determinant == 0:
        return "Zero determinant"
    else:
        return "Negative determinant"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
result = calculate_determinant(a, b, c)
print("Result:", result)
