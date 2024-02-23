n = int(input("Enter the value of n: "))
sequence = [(-1)**(i+1) * 5 * i for i in range(1, n+1)]
print("Sequence:", sequence)
