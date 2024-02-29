# i)
def pattern_i():
    for i in range(1, 5):
        print("* " * i)
    for i in range(3, 0, -1):
        print("* " * i)

# ii)
def pattern_ii():
    for i in range(1, 6):
        for j in range(i, 0, -1):
            print(j, end=" ")
        for j in range(2, i + 1):
            print(j, end=" ")
        print()

# iii)
def pattern_iii():
    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# iv)
def pattern_iv():
    for i in range(5):
        if i == 0 or i == 4:
            print("* ")
        else:
            print("* *")

# Test the patterns
pattern_i()
print("\n")
pattern_ii()
print("\n")
pattern_iii()
print("\n")
pattern_iv()
