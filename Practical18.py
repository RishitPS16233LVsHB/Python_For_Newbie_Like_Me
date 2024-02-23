n = int(input("Enter the value of n: "))
        
series_sum = 0
for i in range(1, n+1):
    series_sum += 1/(i**3) 

print("Sum of series:", series_sum)
