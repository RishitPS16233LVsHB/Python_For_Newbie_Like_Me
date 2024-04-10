class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def add_polynomials(self, other):
        result = []
        for coef1, coef2 in zip(self.coefficients, other.coefficients):
            result.append(coef1 + coef2)
        return result

# Example usage:
poly1 = Polynomial([1, 2, 3])
poly2 = Polynomial([4, 5, 6])
result = poly1.add_polynomials(poly2)
print("Result of addition:", result)
