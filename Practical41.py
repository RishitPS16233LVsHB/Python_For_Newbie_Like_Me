def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median = (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        median = sorted_lst[n//2]
    return median

lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
print("Median:", find_median(lst))
