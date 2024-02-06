import datetime as dt

name = input("what is your name? ")
age = int(input("what is your age? "))

if age >= 100:
    print("you are already 100!")
    exit()


difference = 100 - age
currentDate  = dt.date.today()
hundredYear = currentDate.year + difference

print(name + " will turn 100 in year: " + str(hundredYear))