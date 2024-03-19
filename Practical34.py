def sum_digits(string):
    return sum(int(char) for char in string if char.isdigit())

string = input("Enter string with digits: ")
print("Sum of digits:", sum_digits(string))
