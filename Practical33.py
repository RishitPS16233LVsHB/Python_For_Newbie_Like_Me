def delete_char(string, char):
    return string.replace(char, "")

string = input("Enter string: ")
char = input("Enter character to delete: ")
print("After deleting:", delete_char(string, char))
