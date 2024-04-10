# Example list of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzip list of tuples into individual lists
numbers, letters = zip(*list_of_tuples)

print("Numbers:", numbers)
print("Letters:", letters)
