def insert_string_in_middle(main_string, insert_string):
    middle_index = len(main_string) // 2
    return main_string[:middle_index] + insert_string + main_string[middle_index:]

# Example usage
main_string = "Hello, Sir!"
insert_string = " Hi!"
result = insert_string_in_middle(main_string, insert_string)
print(result)
