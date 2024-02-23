def is_palindrome(number):
    return str(number) == str(number)[::-1]

number = input("Enter a number to check if it's a palindrome: ")
if is_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
