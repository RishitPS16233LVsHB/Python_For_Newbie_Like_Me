# a. Replace '/' with '-' in a date string.
def format_date(date_string):
    return date_string.replace('/', '-')

# b. Count occurrences of a specified character in a string.
def count_occurrences(string, char):
    return string.count(char)

# Example usage:
date = "10/04/2024"
print(format_date(date))
print(count_occurrences("hello world", "o"))
