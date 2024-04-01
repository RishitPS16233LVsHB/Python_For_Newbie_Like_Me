# Read two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform arithmetic operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

# Check if num2 is not 0 for division
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Division by zero is not allowed"

# Print the results
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Division: {div_result}")
