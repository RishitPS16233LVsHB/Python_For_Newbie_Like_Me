# a. Convert milliseconds to hours, minutes and seconds.
def milliseconds_to_time(milliseconds):
    seconds = milliseconds // 1000
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

# b. Compute a sales commission, given the sales amount and the commission rate.
def compute_sales_commission(sales_amount, commission_rate):
    return sales_amount * commission_rate

# c. Convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage:
print(milliseconds_to_time(10000))
print(compute_sales_commission(1000, 0.05))
print(celsius_to_fahrenheit(25))
