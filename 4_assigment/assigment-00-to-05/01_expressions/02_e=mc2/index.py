# Constant value for the speed of light (C)
C = 299792458  # meters per second

def calculate_energy(mass):
    """Calculate energy using Einstein's equation E = m * C^2"""
    return mass * C**2

def main():
    while True:
        try:
            mass = float(input("Enter kilos of mass: "))
            energy = calculate_energy(mass)

            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s\n")
            print(f"{energy} joules of energy!\n")
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()
