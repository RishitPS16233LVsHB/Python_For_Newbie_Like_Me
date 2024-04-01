# Initialize variables
total = 0
number = 100

# Loop through numbers from 100 to 200
while number <= 200:
    # Check if the number is even
    if number % 2 == 0:
        # Add the number to the total
        total += number
    # Move to the next number
    number += 1

# Print the total
print("The sum of even numbers between 100 and 200 is:", total)
