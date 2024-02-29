def check_divisibility(num):
    if num % 7 == 0:
        print(num, "is divisible by 7")
    else:
        print(num, "is not divisible by 7")

number = int(input("Enter a number: "))
check_divisibility(number)
