def check_student_presence(students, name):
    return name in students

def check_student_presence_builtin(students, name):
    return name in students

students = tuple(input("Enter names of students separated by space: ").split())
name_to_check = input("Enter name to check: ")

# Using user-defined function
if check_student_presence(students, name_to_check):
    print(f"{name_to_check} is present in the list of students")
else:
    print(f"{name_to_check} is not present in the list of students")

# Using built-in function
if check_student_presence_builtin(students, name_to_check):
    print(f"{name_to_check} is present in the list of students")
else:
    print(f"{name_to_check} is not present in the list of students")
