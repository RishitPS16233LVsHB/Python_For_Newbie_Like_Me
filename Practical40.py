def second_largest(lst):
    sorted_lst = sorted(set(lst))
    if len(sorted_lst) < 2:
        return "Second largest element does not exist"
    else:
        return sorted_lst[-2]

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
print("Second largest element:", second_largest(lst))
