# Creating a sample dictionary
my_dict = {'A': 123, 'B': 456, 'C': 789}

# Using clear() method
my_dict.clear()
print("Dictionary after clear():", my_dict)

# Using fromkeys() method
keys = ['X', 'Y', 'Z']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("Dictionary from fromkeys():", new_dict)
