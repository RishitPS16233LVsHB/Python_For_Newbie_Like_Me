def swap_numbers(num1, num2):
    if num1 < num2:
        return num2, num1
    else:
        return num1, num2

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

num1, num2 = swap_numbers(num1, num2)
print("Swapped numbers:", num1, num2)
