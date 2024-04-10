def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 48
num2 = 18
print("GCD of", num1, "and", num2, "is:", find_gcd(num1, num2))
