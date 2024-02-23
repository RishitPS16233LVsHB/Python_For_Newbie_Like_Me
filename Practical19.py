number = input("Enter an integer number: ")
# use of list comprehensions
digit_sum = sum([int(digit) for digit in number])
print("Sum of digits:", digit_sum)
