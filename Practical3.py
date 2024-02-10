
# Accept input for the number of days each worker takes to complete the job
x = float(input("Enter days A takes to complete the job: "))
y = float(input("Enter days B takes to complete the job: "))
z = float(input("Enter days C takes to complete the job: "))

# Calculate completion time
completion_time = (x * y * z) / (x * y + y * z + x * z)

# Output the completion time
print("The job will be completed in", int(completion_time), "days when A, B, and C work together.")

