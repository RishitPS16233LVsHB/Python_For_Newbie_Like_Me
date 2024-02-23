def print_table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

number = int(input("Enter a number to print its table: "))
print_table(number)
