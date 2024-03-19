def reverse_list_inplace(lst):
    lst.reverse()

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
reverse_list_inplace(lst)
print("Reversed list:", lst)
