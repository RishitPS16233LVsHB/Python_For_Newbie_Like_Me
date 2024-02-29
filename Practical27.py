def compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate/n)**(n*time)
    ci = amount - principal
    return ci

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))
n = float(input("Enter number of times interest is compounded annually: "))

compound_interest = compound_interest(principal, rate, time, n)
print("Compound Interest:", compound_interest)
