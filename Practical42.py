def remove_duplicates(lst):
    return list(set(lst))

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
print("List with duplicates removed:", remove_duplicates(lst))
