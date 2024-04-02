def print_pascals_triangle(rows):
    for i in range(rows):
        # Calculate the current row of Pascal's triangle
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1)

        # Print the current row
        print(" "*(rows-i-1)*2 + " ".join(map(str, row)))

        # Update the previous row for the next iteration
        prev_row = row

# Get the number of rows from the user
rows = int(input("Enter the number of rows for Pascal's triangle: "))

# Print Pascal's triangle
print_pascals_triangle(rows)
