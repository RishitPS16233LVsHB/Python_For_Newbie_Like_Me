def count_letters(string):
    letter_count = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

# Example usage:
sample_string = 'w3resource'
print("Letter Count:", count_letters(sample_string))
