def count_letter_occurrences(filename):
    letter_count = {}
    with open(filename, "r") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

# Example usage:
filename = "example.txt"
print(count_letter_occurrences(filename))
