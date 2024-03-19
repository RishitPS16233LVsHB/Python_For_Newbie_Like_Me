def highest_2_values(dictionary):
    sorted_values = sorted(dictionary.values(), reverse=True)
    return sorted_values[:2]

my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
print("Highest 2 values:", highest_2_values(my_dict))
