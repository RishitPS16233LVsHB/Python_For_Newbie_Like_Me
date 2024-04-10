def read_first_n_lines(filename, n):
    with open(filename, "r") as file:
        lines = [file.readline().strip() for _ in range(n)]
    return lines

# Example usage:
filename = "example.txt"
n = 3
print(read_first_n_lines(filename, n))
