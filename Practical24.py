def prefix_name(name, gender):
    if gender == "M":
        return "Mr. " + name
    elif gender == "F":
        return "Ms. " + name
    else:
        return name

name = input("Enter name: ")
gender = input("Enter gender (M/F): ")
prefixed_name = prefix_name(name, gender)
print("Prefixed Name:", prefixed_name)
