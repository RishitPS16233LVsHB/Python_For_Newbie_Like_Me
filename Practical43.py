def insert_element(lst, element, position):
    lst.insert(position, element)
    return lst

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
element = int(input("Enter element to insert: "))
position = int(input("Enter position to insert: "))
print("List after insertion:", insert_element(lst, element, position))
