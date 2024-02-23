n = int(input("Enter the value of n: "))
multiplier = -1
for i in range(1,n+1):
    print(str((i * 5 * multiplier)) + " ")
    multiplier *= -1

