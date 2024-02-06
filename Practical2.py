def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    amount_payable = principal + si
    return amount_payable

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (in % per annum): "))
time = float(input("Enter time (in years): "))

amount = calculate_simple_interest(principal, rate, time)
print("Amount payable:", amount)

