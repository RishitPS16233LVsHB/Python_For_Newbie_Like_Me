def replace_string(original, old, new):
    result = ""
    i = 0
    while i < len(original):
        if original[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += original[i]
            i += 1
    return result

# Example usage:
original_string = "hello world"
old_substring = "world"
new_substring = "universe"
print(replace_string(original_string, old_substring, new_substring))
