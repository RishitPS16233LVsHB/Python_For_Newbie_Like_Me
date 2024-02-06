def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Boiling point and freezing point of water in Fahrenheit
boiling_point_f = celsius_to_fahrenheit(100)
freezing_point_f = celsius_to_fahrenheit(0)

print("Boiling point of water in Fahrenheit:", boiling_point_f)
print("Freezing point of water in Fahrenheit:", freezing_point_f)
