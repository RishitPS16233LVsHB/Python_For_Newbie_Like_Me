import datetime as dt

name = input("What is your name? ")
age = int(input("What is your age? "))

if age >= 100:
    print("You are already 100!")
else:
    hundred_year = dt.date.today().year + (100 - age)
    print(name + " will turn 100 in year:", hundred_year)
