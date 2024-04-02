def print_pascals_triangle(rows):
    for i in range(rows):
        # Print leading spaces
        for _ in range(rows - i - 1):
            print(" ", end="")
        
        # Calculate and print values for current row
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        
        # Move to the next line
        print()

# Input the number of rows for Pascal's triangle
rows = int(input("Enter the number of rows for Pascal's triangle: "))

# Display Pascal's triangle
print_pascals_triangle(rows)
