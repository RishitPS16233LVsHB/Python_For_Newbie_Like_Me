set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Updating set1 with items not present in set2
set1.update(set2.difference(set1))
print("Updated Set1:", set1)
