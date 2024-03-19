def create_letter_count_dict(string):
    letter_count = {}
    for char in string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

string = 'w3resource'
print("Letter count dictionary:", create_letter_count_dict(string))
