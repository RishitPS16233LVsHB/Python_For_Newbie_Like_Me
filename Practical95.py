def input_employee_info():
    num_employees = int(input("Enter the number of employees: "))
    employee_data = []
    for i in range(num_employees):
        name = input("Enter employee name: ")
        employee_id = input("Enter employee ID: ")
        salary = float(input("Enter employee salary: "))
        employee_info = {"Name": name, "Employee ID": employee_id, "Salary": salary}
        employee_data.append(employee_info)
    return employee_data

# Example usage:
employees = input_employee_info()
print("Employee Information:")
for employee in employees:
    print(employee)
