numbers = []

for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
