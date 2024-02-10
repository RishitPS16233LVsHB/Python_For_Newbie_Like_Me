# Accept input for principal amount, rate of interest, and time
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (in % per annum): "))
time = float(input("Enter time (in years): "))

# Calculate simple interest and amount payable
si = (principal * rate * time) / 100
amount = principal + si

# Output the amount payable
print("Amount payable:", amount)
