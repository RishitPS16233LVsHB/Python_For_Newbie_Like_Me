import random

# Create a list of 10 random integers
random_integers = [random.randint(1, 100) for _ in range(10)]

# Filter odd and even numbers into separate lists
odd_list = [num for num in random_integers if num % 2 != 0]
even_list = [num for num in random_integers if num % 2 == 0]

print("Random Integers:", random_integers)
print("Odd List:", odd_list)
print("Even List:", even_list)
