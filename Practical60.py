# Question a

n = int(input("Enter the value of n: "))
sum = 0.0
for i in range(1, n + 1):
    sum += 1 / i

print(f"The sum of the series is: {sum}")

# Question b

n = int(input("Enter the value of n: "))
sum = 0.0
for i in range(1, n + 1):
    sum += i / i

print(f"The sum of the series is: {sum}")
