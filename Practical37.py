def separate_positive_negative(lst):
    positive_numbers = [num for num in lst if num >= 0]
    negative_numbers = [num for num in lst if num < 0]
    return positive_numbers, negative_numbers

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
positive_numbers, negative_numbers = separate_positive_negative(lst)
print("Original list:", lst)
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
