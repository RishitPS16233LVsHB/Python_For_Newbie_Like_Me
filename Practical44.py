# Delete element by position
def delete_by_position(lst, position):
    if 0 <= position < len(lst):
        del lst[position]
    else:
        print("Invalid position")

# Delete element by value
def delete_by_value(lst, value):
    if value in lst:
        lst.remove(value)
    else:
        print("Value not found")

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
position = int(input("Enter position of element to delete: "))
delete_by_position(lst, position)
print("List after deletion by position:", lst)

value = int(input("Enter value of element to delete: "))
delete_by_value(lst, value)
print("List after deletion by value:", lst)
