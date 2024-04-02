def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Input values for n and r from user
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

# Calculate and display permutation and combination
print(f"Permutation ({n}P{r}): {permutation(n, r)}")
print(f"Combination ({n}C{r}): {combination(n, r)}")
