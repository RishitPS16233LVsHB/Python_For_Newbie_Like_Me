def largest_element(lst):
    return max(lst)

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
print("Largest element:", largest_element(lst))
