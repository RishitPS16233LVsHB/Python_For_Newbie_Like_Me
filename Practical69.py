def strip_characters(string, chars_to_strip):
    result = ""
    for char in string:
        if char not in chars_to_strip:
            result += char
    return result

# Example usage:
original_string = "hello world"
chars_to_strip = "lo"
print(strip_characters(original_string, chars_to_strip))
