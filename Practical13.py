def check_license_eligibility(name, age):
    if age >= 18:
        print(f"{name}, you are eligible to apply for a driving license.")
    else:
        print(f"Sorry {name}, you are not eligible to apply for a driving license yet.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
check_license_eligibility(name, age)
