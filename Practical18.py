n = int(input("Enter the value of n: "))
series_sum = sum([1/(i**3) for i in range(1, n+1)])
print("Sum of series:", series_sum)
