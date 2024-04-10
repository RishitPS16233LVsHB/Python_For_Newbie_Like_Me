class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def roots(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant > 0:
            root1 = (-self.b + discriminant ** 0.5) / (2 * self.a)
            root2 = (-self.b - discriminant ** 0.5) / (2 * self.a)
            return root1, root2
        elif discriminant == 0:
            root = -self.b / (2 * self.a)
            return root,
        else:
            real_part = -self.b / (2 * self.a)
            imaginary_part = (-discriminant) ** 0.5 / (2 * self.a)
            return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

# Example usage:
equation = Quadratic(1, -3, 2)
print("Roots:", equation.roots())
