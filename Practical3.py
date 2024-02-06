
def calculate_completion_time(x, y, z):
    return (x * y * z) / (x * y + y * z + x * z)

x = float(input("Enter days A takes to complete the job: "))
y = float(input("Enter days B takes to complete the job: "))
z = float(input("Enter days C takes to complete the job: "))

completion_time = calculate_completion_time(x, y, z)
print("The job will be completed in", int(completion_time), "days when A, B, and C work together.")
