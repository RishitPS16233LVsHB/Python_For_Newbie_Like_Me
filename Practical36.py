def count_occurrences(lst, element):
    return lst.count(element)

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
element = int(input("Enter element to count: "))
print("Occurrences:", count_occurrences(lst, element))
