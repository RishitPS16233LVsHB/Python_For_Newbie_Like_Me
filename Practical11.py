def calculate_energy(mass):
    c = 3e8  # speed of light in m/s
    energy = mass * c**2
    return energy

mass = float(input("Enter the mass of the object in kg: "))
energy = calculate_energy(mass)
print("Equivalent energy:", energy, "Joules")
