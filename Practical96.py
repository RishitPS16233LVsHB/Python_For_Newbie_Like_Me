def highest_two_values(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict[:2]

# Example usage:
data = {"A": 100, "B": 200, "C": 150, "D": 50}
print("Highest Two Values:", highest_two_values(data))
